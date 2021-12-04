import csv

import pytest


@pytest.fixture()
def yearly_profits():
    a = []
    with open("resources/prices_yearly.csv", newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            a.append({"time": row["Date"], "price": row["Close"]})
    return a


@pytest.fixture()
def daily_profits():
    a = []
    with open("resources/prices_daily.csv", newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            a.append({"time": row["Date"], "price": row["Close"]})
    return a


@pytest.fixture()
def sp500_yearly():
    a = []
    with open("resources/sp500_yearly.csv", newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            a.append({"time": row["DATE"], "price": row["Close"]})
    return a


@pytest.fixture()
def sp500_daily():
    a = []
    with open("resources/sp500_daily.csv", newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            a.append({"time": row["DATE"], "price": row["Close"]})
    return a
