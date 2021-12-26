
from portfolio_analysis.services.portfolio_coefficients import portfolio_coefficients
from portfolio_analysis.services.portfolio_data import form_portfolio_data


def demo(portfolio, depth=5) -> dict:

    data = form_portfolio_data(portfolio, depth=5)
    resp = portfolio_coefficients(data)
    return resp


def main():
    example_portfolio = [{"name": "mco", "number": 1.0}, {"name": "goog", "number": 0.5}]
    res = demo(example_portfolio)
    for line in res.values():
        print(line)


if __name__ == "__main__":
    main()
