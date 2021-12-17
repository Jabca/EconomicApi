from typing import List, Dict


def average_weighted(data: List[Dict[str, float]]) -> float:
    sum_of_el = 0.0
    amount_of_el = 0.0

    for pair in data:
        sum_of_el += pair["value"] * pair["number"]
        amount_of_el += pair["number"]

    return sum_of_el / amount_of_el

