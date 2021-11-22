def yearly_profits(data: list, depth=10) -> list:
    depth += 1
    yearly_profits = []

    for i in range(1, min(len(data), depth)):
        prev_price = data[i]["price"]
        cur_price = data[i-1]["price"]
        yearly_profits.append({"time": data[i-1]["time"], "profit": (cur_price - prev_price) / prev_price})

    return yearly_profits
