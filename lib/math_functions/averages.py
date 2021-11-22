def average_geometrical(profits: list) -> float:
    ret = 1
    for i in profits:
        ret *= (1 + i["profit"])
    return ret ** (1/len(profits)) - 1


def average_arithmetic(profits: list) -> float:
    tmp = 0
    for el in profits:
        tmp += el["profit"]
    return tmp / len(profits)