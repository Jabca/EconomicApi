import concurrent.futures

from portfolio_analysis.api_interaction.SP500_index import *
from portfolio_analysis.api_interaction.info import *
from portfolio_analysis.api_interaction.prices import *
from portfolio_analysis.data_transform.prices_transform import get_daily_prices, get_yearly_prices
from portfolio_analysis.data_transform.profits import get_profits
from portfolio_analysis.services.coefficients import *


def share_coefficients(ticker: str, depth=5, benchmark_raw=DataFrame()) -> dict:
    """Returns dictionary of all five data_transform args:
        ticker
        depth in years(default=5)
        benchmark_data(by default - sp500 index)"""

    response = dict()
    response["name"] = ticker
    response["depth"] = depth

    inf = dict()
    data_raw = DataFrame()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = list()
        futures.append(executor.submit(get_raw_prices, ticker, depth=depth))
        futures.append(executor.submit(get_company_info, ticker))
        if benchmark_raw.empty:
            futures.append(executor.submit(get_sp500_raw, depth=depth))
        for future in concurrent.futures.as_completed(futures):
            t = future.result()
            if t[0] == "raw_prices":
                data_raw = t[1]
            elif t[0] == "info":
                inf = t[1]
            else:
                sp500_raw = t[1]

    y_profits = get_profits(get_yearly_prices(data_raw, depth=depth))
    d_profits = get_profits(get_daily_prices(data_raw))
    sp500_y = get_profits(get_yearly_prices(sp500_raw, depth=depth))
    sp500_d = get_profits(get_daily_prices(sp500_raw))

    response["sharpe"] = None
    response["variation"] = None
    response["information"] = None
    response["sortino"] = None
    response["treynor"] = None

    if any(map(lambda z: len(z) == 0, (y_profits, d_profits, inf))):
        return response

    response["sharpe"] = sharpe_ratio(y_profits)
    response["variation"] = variation_ratio(y_profits)
    response["information"] = information_ratio(y_profits, sp500_y, d_profits, sp500_d)
    response["sortino"] = sortino_ratio(y_profits, d_profits)


    for key in inf.keys():
        if "beta" in key and inf[key] is not None:
            # print(key, inf[key])
            response["treynor"] = treynor_ratio(y_profits, inf[key])
            break

    return response
