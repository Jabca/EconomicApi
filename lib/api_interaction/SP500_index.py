import pandas_datareader.data as web
from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta
from pandas import DataFrame


def get_sp500_raw(depth: int) -> DataFrame:
    today = datetime.today()
    start = today - relativedelta(years=depth)
    end = today
    sp500 = web.DataReader(['sp500'], 'fred', start, end)
    sp500 = sp500.dropna(axis=0, how='any', inplace=False)
    return sp500


def get_sp500_yearly(depth=5) -> list:
    sp500 = get_sp500_raw(depth)
    today = datetime.today()
    start = today - relativedelta(years=depth)
    sp500_yearly = []
    length = len(sp500) - 1

    for i, (timestamp, row) in enumerate(sp500.iterrows()):
        if start - timestamp.to_pydatetime() < timedelta(days=3) or i == length:
            start += relativedelta(years=1)
            sp500_yearly.append({"time": timestamp.strftime("%Y-%m-%d"), "price": row.sp500})

    return sp500_yearly[::-1]


def get_sp500_daily(depth=5) -> list:
    sp500 = get_sp500_raw(depth)
    sp500_daily = []

    for timestamp, row in sp500.iterrows():
        sp500_daily.append({"time": timestamp.strftime("%Y-%m-%d"), "price": row.sp500})

    return sp500_daily[::-1]

