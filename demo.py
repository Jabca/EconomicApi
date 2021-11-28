import concurrent.futures

from portfolio_analysis.api_interaction.SP500_index import *
from portfolio_analysis.api_interaction.info import *
from portfolio_analysis.api_interaction.prices import *
from portfolio_analysis.data_transform.prices_transfrom import get_daily_prices, get_yearly_prices
from portfolio_analysis.data_transform.profits import get_profits
from portfolio_analysis.services.coefficients import *


def get_share_info(name: str, depth=5) -> dict:
    response = dict()
    response["name"] = name
    response["depth"] = depth

    sp500_raw = DataFrame()
    inf = dict()
    data_raw = DataFrame()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = list()
        futures.append(executor.submit(get_raw_prices, name, depth=depth))
        futures.append(executor.submit(get_sp500_raw, depth=depth))
        futures.append(executor.submit(get_company_info, name))
        for future in concurrent.futures.as_completed(futures):
            t = future.result()
            if t[0] == "raw_prices":
                data_raw = t[1]
            elif t[0] == "sp500_raw":
                sp500_raw = t[1]
            else:
                inf = t[1]

    y_profits = get_profits(get_yearly_prices(data_raw, depth=depth))
    d_profits = get_profits(get_daily_prices(data_raw))
    sp500_y = get_profits(get_yearly_prices(sp500_raw, depth=depth))
    sp500_d = get_profits(get_daily_prices(sp500_raw))

    response["sharpe"] = sharpe_ratio(y_profits)
    response["variation"] = variation_ratio(y_profits)
    response["information"] = information_ratio(y_profits, sp500_y, d_profits, sp500_d)
    response["sortino"] = sortino_ratio(y_profits, d_profits)
    response["treynor"] = treynor_ratio(y_profits, inf["beta"])

    return response


if __name__ == "__main__":
    print(get_share_info("aapl", depth=5))