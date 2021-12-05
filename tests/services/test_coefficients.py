from portfolio_analysis.services.coefficients import *
from tests.test_app import *
from portfolio_analysis.data_transform.abnormal_returns import get_abnormal_returns
from portfolio_analysis.data_transform.abnormal_returns import get_abnormal_returns
from portfolio_analysis.math_functions.standard_deviation import standard_deviation


@pytest.mark.service_op
def test_sharpe(yearly_profits):
    res = sharpe_ratio(yearly_profits)
    exp_res = 1.7849966959331272
    assert abs(res - exp_res) < 1e-5


@pytest.mark.service_op
def test_sortino(yearly_profits, daily_profits):
    res = sortino_ratio(yearly_profits, daily_profits)
    exp_res = 2.440026305044653
    assert abs(res - exp_res) < 1e-5


@pytest.mark.service_op
def test_variations(yearly_profits):
    res = variation_ratio(yearly_profits)
    exp_res = 0.5132842416267016
    assert abs(res - exp_res) < 1e-5


@pytest.mark.service_op
def test_information(yearly_profits, sp500_yearly_profits, daily_profits, sp500_daily_profits):
    res = information_ratio(yearly_profits, sp500_yearly_profits, daily_profits, sp500_daily_profits)
    exp_res = 1.6296454592243053
    assert abs(res - exp_res) < 1e-5


@pytest.mark.service_op
def test_treynor(yearly_profits):
    res = treynor_ratio(yearly_profits, 1.205714)
    exp_res = 0.4228260745970034
    assert abs(res - exp_res) < 1e-5
