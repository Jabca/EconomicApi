import yfinance as yf
from pandas import DataFrame
from datetime import datetime
from typing import Tuple


def get_raw_prices(ticker: str, depth: int) -> Tuple[str, DataFrame]:
    company = yf.Ticker(ticker)
    today = datetime.today()
    company_history = company.history(start=f"{today.year - depth}-{today.month}-{today.day}",
                                      end=f"{today.year}-{today.month}-{today.day}", interval="1d")
    company_history = company_history.dropna(axis=0, how='any', inplace=False)

    return "raw_prices", company_history




