from portfolio_analysis.math_functions.averages import *
from tests.test_app import *


@pytest.mark.easy_operation
def test_arithmetic(test_profits):
    exp_res = 0.38
    res = average_arithmetic(test_profits)
    assert abs(res - exp_res) < 1e-5


@pytest.mark.easy_operation
def test_geometrical(test_profits):
    exp_res = 0.3364579251961
    res = average_geometrical(test_profits)
    assert abs(res - exp_res) < 1e-5
