import yfinance as yf
import datetime


def get_yearly_prices(ticker: str, depth=10) -> list:
    company = yf.Ticker(ticker)
    today = datetime.date.today()
    company_history = company.history(start=f"{today.year-depth}-{today.month}-{today.day}",
                                      end=f"{today.year}-{today.month}-{today.day}", interval='3mo')
    company_history = company_history.dropna(axis=0, how='any', inplace=False)
    # print(company_history)

    yearly_prices = []
    ticker = -1
    for i, row in company_history.iterrows():
        ticker += 1
        ticker %= 4
        if ticker % 4 != 0:
            continue
        yearly_prices.append({"time": i.strftime("%Y-%m-%d"), "price": row.Close})

    return yearly_prices[::-1]

