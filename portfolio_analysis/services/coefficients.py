from portfolio_analysis.math_functions.standard_deviation import standard_deviation
from portfolio_analysis.math_functions.averages import average_geometrical, average_arithmetic
from portfolio_analysis.data_transform.abnormal_returns import get_abnormal_returns
from portfolio_analysis.data_transform.downside import get_downsides


"""This file contain functions that calculate coefficients"""


def variation_ratio(yearly_profits: list) -> float:
    """calculate variation ratio based on array of yearly profits"""

    numerator = standard_deviation(yearly_profits)
    denominator = average_arithmetic(yearly_profits)
    return numerator / denominator


def information_ratio(profits_y: list, benchmark_profits_y: list, profits_d: list, benchmark_profits_d: list) -> float:
    """calculate information ratio based on arrays of:
        share yearly profits,
        benchmark yearly profits,
        share daily profits,
        benchmark daily profits """

    numerator = average_geometrical(profits_y) - average_geometrical(benchmark_profits_y)
    denominator = standard_deviation(get_abnormal_returns(profits_d, benchmark_profits_d)) * 252 ** 0.5
    return numerator / denominator


def sharpe_ratio(profits_y: list, non_risk_return=0.03) -> float:
    """calculate sharpe ratio based on array of yearly profits"""
    numerator = average_geometrical(profits_y) - non_risk_return
    denominator = standard_deviation(profits_y)
    return numerator / denominator


def sortino_ratio(profits_y: list, profit_d: list, non_risk_return=0.03) -> float:
    """calculate sortino ratio based on arrays of
        share yearly profits,
        share daily profits"""

    numerator = average_geometrical(profits_y) - non_risk_return
    denominator = standard_deviation(get_downsides(profit_d)) * 252 ** 0.5
    return numerator / denominator


def treynor_ratio(profits_y: list, beta_coefficient: float, non_risk_return=0.03):
    """calculate treynor ratio based on:
            array of share yearly profits,
            share beta coefficient  """

    numerator = average_geometrical(profits_y) - non_risk_return
    denominator = beta_coefficient
    return numerator / denominator
