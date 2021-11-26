from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta
from pandas import DataFrame


def get_yearly_prices(company_history: DataFrame, depth=5) -> list:
    today = datetime.today()
    start = today - relativedelta(years=depth)
    yearly_prices = []
    length = len(company_history) - 1
    for i, (timestamp, row) in enumerate(company_history.iterrows()):
        if start - timestamp.to_pydatetime() < timedelta(days=3) or i == length:
            start += relativedelta(years=1)
            yearly_prices.append({"time": timestamp.strftime("%Y-%m-%d"), "price": row.Close})

    return yearly_prices[::-1]


def get_daily_prices(company_history: DataFrame) -> list:
    daily_prices = []
    for timestamp, row in company_history.iterrows():
        daily_prices.append({"time": timestamp.strftime("%Y-%m-%d"), "price": row.Close})

    return daily_prices[::-1]
