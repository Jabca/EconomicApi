def standard_deviation(yearly_profits: list) -> float:
    average_profit = 0
    for i in yearly_profits:
        average_profit += i["profit"]
    average_profit /= len(yearly_profits)
    tmp = 0
    for period in yearly_profits:
        tmp += (period["profit"] - average_profit) ** 2

    return (tmp / (len(yearly_profits) - 1)) ** 0.5
