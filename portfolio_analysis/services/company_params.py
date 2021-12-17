from portfolio_analysis.api_interaction.info import get_company_info
from portfolio_analysis.data_transform.prices_transform import get_daily_prices, get_yearly_prices
from portfolio_analysis.data_transform.profits import get_profits
from portfolio_analysis.api_interaction.prices import *

from typing import Dict, Any
import concurrent.futures


def get_company_params(ticker: str, depth=5) -> Dict[str, Any]:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = list()
        futures.append(executor.submit(get_raw_prices, ticker, depth=depth))
        futures.append(executor.submit(get_company_info, ticker))
        for future in concurrent.futures.as_completed(futures):
            t = future.result()
            if type(t) == dict:
                info = t
            else:
                raw_prices = t

    y_prices = get_yearly_prices(raw_prices, depth=depth)
    d_prices = get_daily_prices(raw_prices)
    y_profits = get_profits(y_prices)
    d_profits = get_profits(d_prices)

    return {"info": info, "y_profits": y_profits, "d_profits": d_profits}
