import pandas_datareader.data as web
from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta


def get_sp500_yearly(depth=5) -> list:
    today = datetime.today()
    start = today - relativedelta(years=depth)
    end = today
    sp500 = web.DataReader(['sp500'], 'fred', start, end)
    sp500 = sp500.dropna(axis=0, how='any', inplace=False)
    length = len(sp500) - 1

    sp500_yearly = []
    for i, (timestamp, row) in enumerate(sp500.iterrows()):
        if start - timestamp.to_pydatetime() < timedelta(days=3) or i == length:
            start += relativedelta(years=1)
            sp500_yearly.append({"time": timestamp.strftime("%Y-%m-%d"), "price": row.sp500})

    return sp500_yearly
