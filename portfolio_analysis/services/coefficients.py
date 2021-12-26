from typing import List

from portfolio_analysis.typing_classes import ProfitType
from portfolio_analysis.data_transform.abnormal_returns import get_abnormal_returns
from portfolio_analysis.data_transform.downside import get_downsides
from portfolio_analysis.math_functions.averages import average_geometrical, average_arithmetic
from portfolio_analysis.math_functions.standard_deviation import standard_deviation

"""This file contain functions that calculate data_transform"""


def variation_ratio(yearly_profits: List[ProfitType]) -> float:
    """calculate variation ratio based on array of yearly profits"""

    numerator = standard_deviation(yearly_profits)
    denominator = average_arithmetic(yearly_profits)
    return numerator / denominator


def information_ratio(profits_y: List[ProfitType], benchmark_profits_y: List[ProfitType]) -> float:
    """calculate information ratio based on arrays of:
        share yearly profits,
        benchmark yearly profits """

    numerator = average_geometrical(profits_y) - average_geometrical(benchmark_profits_y)
    denominator = standard_deviation(get_abnormal_returns(profits_y, benchmark_profits_y))
    return numerator / denominator


def sharpe_ratio(profits_y: List[ProfitType], non_risk_return=0.03) -> float:
    """calculate sharpe ratio based on array of yearly profits"""
    numerator = average_geometrical(profits_y) - non_risk_return
    denominator = standard_deviation(profits_y)
    return numerator / denominator


def sortino_ratio(profits_y: List[ProfitType], non_risk_return=0.03) -> float:
    """calculate sortino ratio based on arrays of
        share yearly profits"""

    numerator = average_geometrical(profits_y) - non_risk_return
    denominator = standard_deviation(get_downsides(profits_y, non_risk_return))
    return numerator / denominator


def treynor_ratio(profits_y: List[ProfitType], beta_coefficient: float, non_risk_return=0.03):
    """calculate treynor ratio based on:
            array of share yearly profits,
            share beta coefficient  """

    numerator = average_geometrical(profits_y) - non_risk_return
    denominator = beta_coefficient

    return numerator / denominator
