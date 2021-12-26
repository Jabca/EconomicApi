from portfolio_analysis.typing_classes import ProfitType
from typing import List


def get_downsides(daily_profits: List[ProfitType], target_return: float = 0.0) -> List[ProfitType]:
    """return array of prices, but replacing profits over target return with 0"""

    downsides = []
    for el in daily_profits:
        if el["profit"] < target_return:
            downsides.append({"time": el["time"], "profit": el["profit"]})
        else:
            downsides.append({"time": el["time"], "profit": 0})

    return downsides

