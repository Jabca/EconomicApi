import concurrent.futures
from typing import Dict

from portfolio_analysis.typing_classes import PortfolioInfoType, ResponseType
from portfolio_analysis.api_interaction.SP500_index import get_sp500_raw
from portfolio_analysis.data_transform.prices_transform import get_yearly_prices_from_array
from portfolio_analysis.data_transform.weight_prices import weight_sum_of_prices
from portfolio_analysis.services import company_coefficients


def portfolio_coefficients(portfolio_info: PortfolioInfoType) -> Dict[str, ResponseType]:
    """Example input:
        {"depth": 5,
        "data_sets" :{
            "company1_ticker": {"number": 1.0, "company_params": company_params_dict},
            "company2_ticker": {"number": 2.0, "company_params": company_params_dict}},
        "benchmark": None(if you want to use sp500 as default)
        or prices_dict(if tou want to use smt else as benchmark)}
    """

    depth = portfolio_info["depth"]
    if portfolio_info["benchmark"] is None:
        portfolio_info["benchmark"] = get_sp500_raw(depth=depth)

    portfolio_info["benchmark"]

    portfolio_d_prices = weight_sum_of_prices(portfolio_info["data_sets"])
    portfolio_data = dict()
    portfolio_data["name"] = "portfolio"
    portfolio_data["depth"] = depth
    portfolio_data["d_prices"] = portfolio_d_prices
    portfolio_data["y_prices"] = get_yearly_prices_from_array(portfolio_d_prices, depth=depth)
    portfolio_data["info"] = {}

    portfolio_info["data_sets"]["portfolio"] = {"company_params": portfolio_data}

    response = dict()

    with concurrent.futures.ThreadPoolExecutor() as exe:
        futures = list()
        for company_ticker in portfolio_info["data_sets"].keys():
            company_params = portfolio_info["data_sets"][company_ticker]["company_params"]
            futures.append(exe.submit(company_coefficients,
                                      company_params,
                                      benchmark_raw=portfolio_info["benchmark"],
                                      depth=depth))
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            response[res["name"]] = res

    return response



