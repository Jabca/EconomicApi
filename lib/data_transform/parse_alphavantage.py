def yearly_profits_w_dividends(data: dict, years_count=5) -> list:
    yearly_profits = []
    time_stamps = list(data.keys())
    n = len(time_stamps)

    if n > years_count * 12:
        time_stamps = time_stamps[:years_count * 12]
        n = years_count * 12

    for i in range(0, n - 12, 12):
        this_period = float(data[time_stamps[i]]["5. adjusted close"])
        prev_period = float(data[time_stamps[i+12]]["5. adjusted close"])
        profit = (this_period - prev_period) / prev_period
        yearly_profits.append({"profit": profit, "time": time_stamps[i]})

    return yearly_profits
