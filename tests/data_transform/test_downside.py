from tests.test_app import *
from portfolio_analysis.data_transform.downside import get_downsides


@pytest.mark.data_transform_op
def test_downsides(yearly_downsides, yearly_profits):
    exp_res = yearly_downsides
    res = get_downsides(yearly_profits)
    compare_dictionaries(exp_res, res, key="profit")