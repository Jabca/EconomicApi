def get_abnormal_returns(profits: list, benchmark_profits: list) -> list:
    """return array of difference between profits of share and benchmark.
        args:
            array of share profits,
            array of benchmark profits
        """

    abnormal_returns = []
    for p, b in zip(profits, benchmark_profits):
        abnormal_returns.append({"time": p["time"], "profit": p["profit"] - b["profit"]})

    return abnormal_returns
