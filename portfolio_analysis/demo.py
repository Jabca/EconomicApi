from portfolio_analysis.services.main_service import *


def demo(name: str, depth=5) -> dict:
    response = share_coefficients(name, depth=depth)
    return response


def main():
    print(demo("aapl", depth=3))


if __name__ == "__main__":
    main()
