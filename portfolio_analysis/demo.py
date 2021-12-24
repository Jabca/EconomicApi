
from portfolio_analysis.services.portfolio_coefficients import portfolio_coefficients
from portfolio_analysis.services.portfolio_data import form_portfolio_data


def demo() -> dict:
    example_portfolio = [{"name": "mco", "number": 1.0}, {"name": "goog", "number": 0.5}]

    data = form_portfolio_data(example_portfolio, depth=5)
    # print(data["data_sets"]["aapl"]["company_params"]["info"])
    # print(data)
    resp = portfolio_coefficients(data)
    return resp


def main():
    res = demo()
    for line in res.values():
        print(line)


if __name__ == "__main__":
    main()
