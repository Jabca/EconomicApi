from portfolio_analysis import form_portfolio_data
from portfolio_analysis import portfolio_coefficients


class Portfolio:
    def __init__(self, portfolio_info=None, depth=5):
        self.depth=depth
        if portfolio_info is None:
            self.portfolio_info = list()
        else:
            self.portfolio_info = portfolio_info
        self.portfolio_data = dict()
        self.portfolio_coefficients = dict()

    def update_coefficients(self):
        self.portfolio_coefficients = portfolio_coefficients(self.portfolio_data)

    def update_data(self):
        self.portfolio_data = form_portfolio_data(self.portfolio_info, self.depth)

    def full_update(self):
        self.update_data()
        self.update_coefficients()

    def add_company(self, name: str, number: float):
        if name in [el["name"] for el in self.portfolio_info]:
            return "Already in portfolio"
        self.portfolio_info.append({"name": name, "number": number})

    def get_logo_url(self, name: str):
        return \
            self.portfolio_data["data_sets"][name]["company_params"]["info"]["logo_url"]

    def delete_company(self, name):
        for el in self.portfolio_info:
            if el["name"] == name:
                self.portfolio_info.remove(el)
                return None
        return "Company not in portfolio"
