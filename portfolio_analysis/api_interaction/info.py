import yfinance as yf
from typing import Tuple


def get_company_info(ticker: str) -> Tuple[str, dict]:
    """return dictionary of info about company"""
    info = yf.Ticker(ticker).info
    return "info", info
