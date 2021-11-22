import yfinance as yf
from pandas import DataFrame
from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta


def get_raw_prices(ticker: str, depth: int, interval: str) -> DataFrame:
    company = yf.Ticker(ticker)
    today = datetime.today()
    company_history = company.history(start=f"{today.year - depth}-{today.month}-{today.day}",
                                      end=f"{today.year}-{today.month}-{today.day}", interval=interval)
    company_history = company_history.dropna(axis=0, how='any', inplace=False)

    return company_history


def get_yearly_prices(ticker: str, depth=10) -> list:
    company_history = get_raw_prices(ticker, depth, "1d")
    today = datetime.today()
    start = today - relativedelta(years=depth)
    yearly_prices = []
    length = len(company_history) - 1
    for i, (timestamp, row) in enumerate(company_history.iterrows()):
        if start - timestamp.to_pydatetime() < timedelta(days=3) or i == length:
            start += relativedelta(years=1)
            yearly_prices.append({"time": timestamp.strftime("%Y-%m-%d"), "price": row.Close})

    return yearly_prices[::-1]


def get_daily_prices(ticker: str, depth=10) -> list:
    company_history = get_raw_prices(ticker, depth, "1d")

    daily_prices = []
    for timestamp, row in company_history.iterrows():
        daily_prices.append({"time": timestamp.strftime("%Y-%m-%d"), "price": row.Close})

    return daily_prices[::-1]

