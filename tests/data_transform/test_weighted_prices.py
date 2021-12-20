import pytest

from tests.test_app import *
from portfolio_analysis.data_transform.weight_prices import weight_sum_of_prices


@pytest.mark.data_transform_op
def test_weighted_prices(yearly_prices, yearly_prices_2, weighted_prices):
    input = \
        {"company1_ticker":
             {"number": 1.0, "company_params": {
                 "d_prices": yearly_prices
             }},
         "company2_ticker":
             {"number": 2.0, "company_params": {
                 "d_prices": yearly_prices_2
             }}}
    res = weight_sum_of_prices(input)
    exp_res = weighted_prices
    compare_dictionaries(res, exp_res)
