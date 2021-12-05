from tests.test_app import *
from portfolio_analysis.data_transform.abnormal_returns import get_abnormal_returns


@pytest.mark.data_transform_op
def test_abnormal_returns(abnormal_returns, sp500_daily_profits, daily_profits):
    exp_res = abnormal_returns
    res = get_abnormal_returns(daily_profits, sp500_daily_profits)
    compare_dictionaries(res, exp_res, key="profit")