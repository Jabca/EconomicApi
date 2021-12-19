from typing import List, Dict


def weighted_sum(data: List[Dict[str, float]]) -> float:
    sum_of_el = 0.0

    for pair in data:
        sum_of_el += pair["value"] * pair["number"]

    return sum_of_el

