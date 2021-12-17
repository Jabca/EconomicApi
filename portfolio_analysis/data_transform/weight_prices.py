from typing import List, Dict, Any
from portfolio_analysis.math_functions.weighted_average import average_weighted


def weight_prices(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Returns weighted profits of portfolio
    Example of input
    input = [
        {"number": 1, "profits":
            [{"time": "01", "profit": 1}, {"time": "02", "profit": 2}]
        },
        {"number": 2, "profits":
            [{"time": "01", "profit": -1}, {"time": "02", "profit": -2}]
        }
    }
    """
    cur_day = []
    companies = len(data)
    for comp in range(companies):
        cur_day.append({"number": data[comp]["number"], "value": 0.0})

    result = []
    for day in range(len(data[0]["profits"])):
        for comp in range(companies):
            cur_day[comp]["value"] = data[comp]["profits"][day]["profit"]

        time = data[0]["profits"][day]["time"]
        profit = average_weighted(cur_day)
        result.append({"time": time, "profit": profit})

    return result


p1 = [{"time": "01", "profit": 1}, {"time": "02", "profit": 2}]
p2 = [{"time": "01", "profit": -1}, {"time": "02", "profit": -2}]
d = [{"number": 1, "profits": p1}, {"number": 2, "profits": p2}]

print(weight_prices(d))