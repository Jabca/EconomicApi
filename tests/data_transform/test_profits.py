import pytest

from tests.test_app import *
from portfolio_analysis.data_transform.profits import get_profits


@pytest.mark.data_transform_op
def test_profits(daily_prices, daily_profits):
    exp_res = daily_profits
    res = get_profits(daily_prices)
    compare_dictionaries(exp_res, res, key="profit")
