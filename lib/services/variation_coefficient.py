from lib.math_functions.standard_deviation import standard_deviation


def variation_coefficient(yearly_profits: list) -> float:
    average_profit = 0
    for i in yearly_profits:
        average_profit += i["profit"]
    average_profit /= len(yearly_profits)
    return standard_deviation(yearly_profits) / average_profit

