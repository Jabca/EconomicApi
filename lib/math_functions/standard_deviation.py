from .averages import average_arithmetic


def standard_deviation(profits: list) -> float:
    average_profit = average_arithmetic(profits)
    tmp = 0
    for period in profits:
        tmp += (period["profit"] - average_profit) ** 2

    return (tmp / (len(profits) - 1)) ** 0.5
