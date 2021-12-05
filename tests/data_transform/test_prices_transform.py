from portfolio_analysis.data_transform.prices_transform import *
from tests.test_app import *


@pytest.mark.data_transform_op
def test_transform_yearly_prices(raw_daily, yearly_prices, test_day):
    res = get_yearly_prices(raw_daily, test_day=test_day)
    exp_res = yearly_prices
    compare_dictionaries(res, exp_res)


@pytest.mark.data_transform_op
def test_transform_daily_prices(raw_daily, daily_prices):
    res = get_daily_prices(raw_daily)
    exp_res = daily_prices
    compare_dictionaries(res, exp_res)
