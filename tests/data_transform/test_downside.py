from tests.test_app import *
from portfolio_analysis.data_transform.downside import get_downsides


@pytest.mark.data_transform_op
def test_downsides(daily_downsides, daily_profits):
    exp_res = daily_downsides
    res = get_downsides(daily_profits)
    compare_dictionaries(exp_res, res, key="profit")