from portfolio_analysis.services.portfolio_coefficients import portfolio_coefficients
from portfolio_analysis.services.portfolio_data import form_portfolio_data


def demo(a, depth=5) -> dict:
    data = form_portfolio_data(a, depth=depth)
    # print(data)
    resp = portfolio_coefficients(data)
    return resp


example_portfolio = [{"name": "aapl", "number": 1.0}, {"name": "goog", "number": 0.5}]


def main():
    res = demo(example_portfolio, depth=5)
    for line in res.values():
        print(line)


if __name__ == "__main__":
    main()
