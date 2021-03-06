import pandas_datareader.data as web
from datetime import datetime
from dateutil.relativedelta import relativedelta
from pandas import DataFrame
from typing import Tuple


def get_sp500_raw(depth: int) -> DataFrame:
    """return DataFrame of daily S&P 500 index from yesterday to yesterday - depth_in_years"""

    today = datetime.today()
    start = today - relativedelta(years=depth)
    end = today
    sp500 = web.DataReader(['sp500'], 'fred', start, end)
    sp500 = sp500.dropna(axis=0, how='any', inplace=False)
    sp500 = sp500.rename({"sp500": "Close"}, axis="columns")
    return sp500



