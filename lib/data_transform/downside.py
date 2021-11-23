def get_downsides(daily_profits: list) -> list:
    downsides = []
    for el in daily_profits:
        if el["profit"] < 0:
            downsides.append({"time": el["time"], "profit": el["profit"]})
        else:
            downsides.append({"time": el["time"], "profit": 0})

    return downsides

