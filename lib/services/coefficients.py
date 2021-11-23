from lib.math_functions.standard_deviation import standard_deviation
from lib.math_functions.averages import average_geometrical, average_arithmetic
from lib.data_transform.abnormal_returns import get_abnormal_returns

us_bonds_profits = 0.03


def variation_coefficient(yearly_profits: list) -> float:
    numerator = standard_deviation(yearly_profits)
    denominator = average_arithmetic(yearly_profits)
    return numerator / denominator


def information_coefficient(profits_y: list, benchmark_profits_y: list, profits_d: list, benchmark_profits_d: list) -> float:
    numerator = average_geometrical(profits_y) - average_geometrical(benchmark_profits_y)
    denominator = standard_deviation(get_abnormal_returns(profits_d, benchmark_profits_d)) * 252 ** 0.5
    return numerator / denominator


def sharpe_coefficient(profits_y: list) -> float:
    numerator = average_geometrical(profits_y) - us_bonds_profits
    denominator = standard_deviation(profits_y)
    return numerator / denominator
