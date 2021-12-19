from datetime import timedelta, datetime

from dateutil.relativedelta import relativedelta
from pandas import DataFrame


def get_yearly_prices(company_history: DataFrame, depth=5, test_day=datetime.today()) -> list:
    """get array of yearly prices from pandas DataFrame of daily prices"""

    cur_date = test_day - relativedelta(years=depth)
    yearly_prices = []
    for _ in range(depth + 1):
        row = company_history.iloc[company_history.index.get_loc(cur_date, method='nearest')]
        yearly_prices.append({"time": row.name.strftime("%Y-%m-%d"), "price": row.Close})
        cur_date += relativedelta(years=1)

    return yearly_prices[::-1]


def get_yearly_prices_from_array(company_history: list, depth=5, test_day=datetime.today()) -> list:
    today = test_day
    start = today
    yearly_prices = []
    length = len(company_history)
    i = 0
    while i < length and len(yearly_prices) != depth+1:
        time = company_history[i]["time"]
        timestamp = datetime.strptime(time[2:], "%y-%m-%d")
        if timestamp == start or timestamp - start < timedelta(days=0) or i == length-1:
            start -= relativedelta(years=1)
            price = company_history[i]["price"]
            yearly_prices.append({"time": time, "price": price})
        i += 1

    return yearly_prices


def get_daily_prices(company_history: DataFrame) -> list:
    """get array of daily prices from pandas DataFrame of daily prices"""

    daily_prices = []
    for timestamp, row in company_history.iterrows():
        daily_prices.append({"time": timestamp.strftime("%Y-%m-%d"), "price": row.Close})

    return daily_prices[::-1]
