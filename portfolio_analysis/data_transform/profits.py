def get_profits(data: list) -> list:
    """return array of profits for given period from array of prices"""

    profits = []

    for i in range(1, len(data)):
        prev_price = data[i]["price"]
        cur_price = data[i-1]["price"]
        profits.append({"time": data[i-1]["time"], "profit": (cur_price - prev_price) / prev_price})

    return profits
