import concurrent.futures
from typing import List

from portfolio_analysis.services.company_params import get_company_params
from portfolio_analysis.typing_classes import PortfolioInfoType, PortfolioDataType


def form_portfolio_data(portfolio_info: List[PortfolioInfoType], depth=5) -> PortfolioDataType:
    """
    Returns portfolio data from portfolio description and depth in years(optional)
    example input:
        [{"name": "aapl", "number": 1.0},
        {"name": "goog", "number": 1.0}]
    """
    resp = {"depth": depth,
            "data_sets": {},
            "benchmark": None}

    tmp_dict = dict()
    for pair in portfolio_info:
        tmp_dict[pair["name"]] = pair["number"]

    with concurrent.futures.ThreadPoolExecutor() as exe:
        futures = list()
        for el in portfolio_info:
            futures.append(exe.submit(get_company_params, el["name"], depth=depth))

        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            if res is not None:
                resp["data_sets"][res["name"]] = {"number": tmp_dict[res["name"]], "company_params": res}

    return resp

