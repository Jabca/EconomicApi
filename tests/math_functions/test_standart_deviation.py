from tests.test_app import *
from portfolio_analysis.math_functions.standard_deviation import standard_deviation


@pytest.mark.easy_operation
def test_standard_deviation(test_profits):
    exp_res = 0.354400902933387
    res = standard_deviation(test_profits)
    assert abs(res-exp_res) < 1e-5
