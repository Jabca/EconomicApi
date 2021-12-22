import requests.exceptions
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from requests import get

from gui.portfolio import Portfolio
from gui.table_model import TableModel


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('gui/resources/main_window.ui', self)
        self.portfolio = Portfolio()
        self.loading_gif = QtGui.QMovie()
        self.list_model = QtGui.QStandardItemModel()
        self.table_model = TableModel([[None, None, None, None, None]],
                                      headers=["SHARPE", "VARIATION", "INFORM", "SORTINO", "TREYNOR"])
        self.init_ui()

    def init_ui(self):
        self.companies_list.setModel(self.list_model)
        self.coefficients_table.setModel(self.table_model)
        self.submit_button.clicked.connect(self.add_company_from_form)
        self.update_button.clicked.connect(self.update_table)

        header = self.coefficients_table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)

    def add_company_from_form(self):
        name = self.line_edit.text()
        number = self.doubleSpinBox.value()
        self.portfolio.add_company(name, number)
        self.portfolio.full_update()
        print(f"{name} added")
        it = QtGui.QStandardItem(f"Name: {name}\nNumber: {str(number)}")
        self.list_model.appendRow(it)
        try:
            image = get(self.portfolio.get_logo_url(name), stream=True)
            image = image.content
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(image)
        except requests.exceptions.MissingSchema:
            pixmap = QtGui.QPixmap("gui/resources/placeholder.png")

        if pixmap.height() > pixmap.width():
            pixmap = pixmap.scaledToHeight(64)
        else:
            pixmap = pixmap.scaledToWidth(64)
        it.setData(pixmap, QtCore.Qt.DecorationRole)

    def update_table(self):
        self.table_model.set_data(self.portfolio.portfolio_coefficients)
