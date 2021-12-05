import csv

import pandas
import datetime
import pytest
from pandas import read_csv
from pandas import to_datetime

@pytest.fixture()
def yearly_prices():
    a = []
    with open("tests/resources/prices_yearly.csv", newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            a.append({"time": row["Date"], "price": float(row["Close"])})
    return a[::-1]


@pytest.fixture()
def daily_prices():
    a = []
    with open("tests/resources/prices_daily.csv", newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            a.append({"time": row["Date"], "price": float(row["Close"])})
    return a[::-1]


@pytest.fixture()
def sp500_yearly():
    a = []
    with open("tests/resources/sp500_yearly.csv", newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            a.append({"time": row["DATE"], "price": float(row["Close"])})
    return a[::-1]


@pytest.fixture()
def sp500_daily():
    a = []
    with open("tests/resources/sp500_daily.csv", newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            a.append({"time": row["DATE"], "price": float(row["Close"])})
    return a[::-1]


@pytest.fixture()
def raw_daily():
    with open("tests/resources/prices_daily.csv") as file:
        res = read_csv(file, sep=';')
    res["Date"] = to_datetime(res["Date"])
    res.set_index("Date", inplace=True)
    return res


@pytest.fixture()
def test_day():
    return datetime.datetime(year=2021, month=12, day=2)


def compare_dictionaries(d1, d2, price_diff=1e-3):
    for c1, c2 in zip(d1, d2):
        # print(c1, c2)
        assert (abs(c1["price"] - c2["price"]) < price_diff)
        assert (c1["time"] == c2["time"])

