from .averages import average_arithmetic
from typing import List
from portfolio_analysis.typing_classes import ProfitType


def standard_deviation(profits: List[ProfitType], full: bool = True) -> float:
    average_profit = average_arithmetic(profits)
    tmp = 0
    for period in profits:
        tmp += (period["profit"] - average_profit) ** 2
    if full:
        return (tmp / (len(profits))) ** 0.5
    else:
        return (tmp / (len(profits) - 1)) ** 0.5
