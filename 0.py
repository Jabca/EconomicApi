import requests
from lib.services.variation_coefficient import variation_coefficient
from lib.data_transform.parse_alphavantage import yearly_profits_w_dividends

with open('key.txt') as file:
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=AAPl&interval=5m&apikey={file.readlines()[0]}'

r = requests.get(url)
data = r.json()
print(data)
y_p = yearly_profits_w_dividends(data["Monthly Adjusted Time Series"], years_count=11)
print(*y_p, sep='\n')
print(variation_coefficient(y_p))