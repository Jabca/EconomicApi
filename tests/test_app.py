import csv

import pandas
import datetime
import pytest
from pandas import read_csv
from pandas import to_datetime


def scan_file(name: str, key_row: str, key_col) -> list:
    a = []
    with open(f"tests/resources/{name}", newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            a.append({"time": row["Date"], key_col: float(row[key_row])})
    return a


@pytest.fixture()
def yearly_prices():
    return scan_file("prices_yearly.csv", "Close", "price")[::-1]


@pytest.fixture()
def daily_prices():
    return scan_file("prices_daily.csv", "Close", "price")[::-1]


@pytest.fixture()
def sp500_yearly():
    return scan_file("sp500_yearly.csv", "Close", "price")[::-1]


@pytest.fixture()
def sp500_daily():
    return scan_file("sp500_yearly.csv", "Close", "price")[::-1]


@pytest.fixture()
def daily_profits():
    return scan_file("profits_daily.csv", "profit", "profit")[::-1]


@pytest.fixture()
def raw_daily():
    with open("tests/resources/prices_daily.csv") as file:
        res = read_csv(file, sep=';')
    res["Date"] = to_datetime(res["Date"])
    res.set_index("Date", inplace=True)

    return res


@pytest.fixture()
def test_profits():
    data = [0.7, 0.1, 0.0, 0.9, 0.2]
    t_data = []
    for i in data:
        t_data.append({"time": "2021-12-04", "profit": i})
    return t_data


@pytest.fixture()
def test_day():
    return datetime.datetime(year=2021, month=12, day=2)


def compare_dictionaries(d1, d2, price_diff=1e-3, key="price"):
    for c1, c2 in zip(d1, d2):
        # print(c1, c2)
        assert (abs(c1[key] - c2[key]) < price_diff)
        assert (c1["time"] == c2["time"])

