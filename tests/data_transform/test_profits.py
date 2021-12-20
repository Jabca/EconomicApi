import pytest

from tests.test_app import *
from portfolio_analysis.data_transform.profits import get_profits


@pytest.mark.data_transform_op
def test_profits(yearly_prices, yearly_profits):
    exp_res = yearly_profits
    res = get_profits(yearly_prices)
    compare_dictionaries(exp_res, res, key="profit")
