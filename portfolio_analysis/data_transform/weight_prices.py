from typing import List, Dict, Any
from portfolio_analysis.math_functions.weighted_sum import weighted_sum
from portfolio_analysis.typing_classes import CompanyPortfolioInfoType, PriceType


def weight_sum_of_prices(data: Dict[str, CompanyPortfolioInfoType]) -> List[PriceType]:
    """Returns weighted sum of portfolio prices for every day
    Example of input
        {"company1_ticker": {"number": 1.0, "company_params": company_params_dict},
        "company2_ticker": {"number": 2.0, "company_params": company_params_dict}}
    """
    cur_day = []
    first_company = list(data.keys())[0]
    length = len(data[first_company]["company_params"]["d_prices"])
    days = [d["time"] for d in data[first_company]["company_params"]["d_prices"]]
    for company in data.keys():
        cur_day.append({"number": data[company]["number"], "value": 0.0})

    result = []
    for day in range(length):
        i = 0
        for comp in data.keys():
            cur_day[i]["value"] = data[comp]["company_params"]["d_prices"][day]["price"]
            i += 1

        time = days[day]
        profit = weighted_sum(cur_day)
        result.append({"time": time, "price": profit})

    return result

