from typing import Dict, Union, List, Optional
from portfolio_analysis.typing_classes import CompanyParamsType, ResponseType

from pandas import DataFrame

from portfolio_analysis.api_interaction.SP500_index import get_sp500_raw
from portfolio_analysis.data_transform.prices_transform import get_daily_prices, get_yearly_prices
from portfolio_analysis.data_transform.profits import get_profits
from portfolio_analysis.services.coefficients import *


def company_coefficients(company_params: CompanyParamsType, depth=5,
                         benchmark_raw=DataFrame()) -> ResponseType:
    """Returns dictionary of company coefficients(by default benchmark = sp500)"""

    response = dict()
    response["name"] = company_params["name"]
    response["depth"] = depth

    if benchmark_raw.empty:
        benchmark_raw = get_sp500_raw(depth=depth)

    benchmark_y = get_profits(get_yearly_prices(benchmark_raw, depth=depth))
    benchmark_d = get_profits(get_daily_prices(benchmark_raw))

    y_profits = get_profits(company_params["y_prices"])
    d_profits = get_profits(company_params["d_prices"])

    inf = company_params["info"]

    response["sharpe"] = None
    response["variation"] = None
    response["information"] = None
    response["sortino"] = None
    response["treynor"] = None

    if any(map(lambda z: len(z) == 0, (y_profits, d_profits))):
        return response

    response["sharpe"] = sharpe_ratio(y_profits)
    response["variation"] = variation_ratio(y_profits)
    response["information"] = information_ratio(y_profits, benchmark_y)
    response["sortino"] = sortino_ratio(y_profits)

    for key in inf.keys():
        if "beta" in key and inf[key] is not None:
            response["treynor"] = treynor_ratio(y_profits, inf[key])
            break

    return response
