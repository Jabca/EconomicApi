from portfolio_analysis.typing_classes import ProfitType
from typing import List


def get_abnormal_returns(profits: List[ProfitType], benchmark_profits: List[ProfitType]) -> List[ProfitType]:
    """return array of difference between profits of share and benchmark.
        args:
            array of share profits,
            array of benchmark profits
        """

    abnormal_returns = []
    for p, b in zip(profits, benchmark_profits):
        abnormal_returns.append({"time": p["time"], "profit": p["profit"] - b["profit"]})

    return abnormal_returns
