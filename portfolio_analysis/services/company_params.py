from portfolio_analysis.api_interaction.info import get_company_info
from portfolio_analysis.data_transform.prices_transform import get_daily_prices, get_yearly_prices
from portfolio_analysis.api_interaction.prices import *

from typing import Union
from portfolio_analysis.typing_classes import CompanyParamsType
import concurrent.futures


def get_company_params(ticker: str, depth=5) -> Union[CompanyParamsType, None]:
    """Return info about company(name, info return, daily prices, yearly prices)"""
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

    if raw_prices is None:
        return None

    d_prices = get_daily_prices(raw_prices)
    y_prices = get_yearly_prices(raw_prices, depth=depth)

    return {"name": ticker,
            "info": info,
            "d_prices": d_prices,
            "y_prices": y_prices}

