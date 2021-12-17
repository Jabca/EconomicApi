from portfolio_analysis.services.company_coefficients import company_coefficients


def demo(name: str, depth=5) -> dict:
    response = company_coefficients(name, depth=depth)
    return response


def main():
    print(demo("aapl", depth=5))


if __name__ == "__main__":
    main()
