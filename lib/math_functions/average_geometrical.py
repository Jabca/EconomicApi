def average_geometrical(profits: list) -> float:
    ret = 1
    for i in profits:
        ret *= (1 + i["profit"])
    return ret ** (1/len(profits)) - 1