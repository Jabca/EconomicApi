from portfolio_analysis import form_portfolio_data
from portfolio_analysis import portfolio_coefficients


class Portfolio:
    def __init__(self, portfolio_info=None, depth=5):
        self.depth = depth
        if portfolio_info is None:
            self.portfolio_info = list()
        else:
            self.portfolio_info = portfolio_info
        self.portfolio_data = dict()
        self.portfolio_coefficients = []

    def update_coefficients(self):
        p_c = portfolio_coefficients(self.portfolio_data)
        if p_c is None:
            return None
        self.portfolio_coefficients.clear()
        self.portfolio_coefficients.append(p_c["portfolio"])
        p_c.pop("portfolio")
        for el in sorted(list(p_c.values()), key=lambda z: z["sharpe"], reverse=True):
            self.portfolio_coefficients.append(el)

    def update_data(self):
        self.portfolio_data = form_portfolio_data(self.portfolio_info, self.depth)

    def full_update(self):
        if len(self.portfolio_info) == 0:
            self.portfolio_data = dict()
            self.portfolio_coefficients = []
            return None
        self.update_data()
        self.update_coefficients()

    def add_company(self, name: str, number: float):
        if name in [el["name"] for el in self.portfolio_info]:
            return "Already in portfolio"
        self.portfolio_info.append({"name": name, "number": number})

    def company_in_data(self, name):
        for key in self.portfolio_data["data_sets"]:
            if key == name:
                return True
        return False

    def get_logo_url(self, name: str):
        return \
            self.portfolio_data["data_sets"][name]["company_params"]["info"]["logo_url"]

    def delete_company(self, name):
        for el in self.portfolio_info:
            if el["name"] == name:
                self.portfolio_info.remove(el)
                return None
        return "Company not in portfolio"

    def update_item(self, name, number):
        for el in self.portfolio_info:
            if el["name"] == name:
                el["number"] = number
                break
