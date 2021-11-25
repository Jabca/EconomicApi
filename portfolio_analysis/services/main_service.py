from portfolio_analysis.api_interaction.prices import *
from portfolio_analysis.api_interaction.SP500_index import *
from portfolio_analysis.data_transform.profits import get_profits
from .coefficients import *


def get_share_info(name: str, depth=5) -> dict:
    response = dict()
    response["name"] = name
    y_profits = get_profits(get_yearly_prices(name, depth=depth))
    d_profits = get_profits(get_daily_prices(name, depth=depth))
    sp500_y = get_profits(get_sp500_yearly(depth))
    sp500_d = get_profits(get_sp500_daily(depth))
    response["sharpe"] = sharpe_coefficient(y_profits)
    response["variation"] = variation_coefficient(y_profits)
    response["information"] = information_coefficient(y_profits, sp500_y, d_profits, sp500_d)
    response["sortino"] = sortino_coefficient(y_profits, d_profits)

    return response
