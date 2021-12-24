import requests.exceptions
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from requests import get

from gui.dialog_box import EditDialog
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
        # self.update_button.clicked.connect(self.update_table)
        self.companies_list.doubleClicked.connect(self.on_edit)
        self.companies_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.update_button.clicked.connect(self.update)
        self.depth_years.valueChanged.connect(self.update_depth)
        self.setWindowTitle("Stock company coefficients")

        header = self.coefficients_table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)

    def add_company_from_form(self):
        name = self.line_edit.text()
        number = self.doubleSpinBox.value()
        if self.portfolio.add_company(name, number) is not None:
            return None
        self.portfolio.full_update()
        if not self.portfolio.company_in_data(name):
            self.portfolio.delete_company(name)
            return None
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
        self.update_table()
        self.line_edit.clear()
        print(f"{name} added")

    def update_table(self):
        self.table_model.set_data(self.portfolio.portfolio_coefficients)
        print("table updated")

    def update(self) -> None:
        self.portfolio.full_update()
        self.update_table()
        print("full update")

    def update_depth(self):
        self.portfolio.depth = self.depth_years.value()

    def keyPressEvent(self, event):
        if event.key() == 16777220:
            self.add_company_from_form()

    def on_edit(self, index):
        item = self.list_model.itemFromIndex(index)
        text = item.text()
        text = text.replace("\n", ": ")
        items = text.split(": ")
        name = items[1]
        number = float(items[3])
        dlg = EditDialog(name, number)
        return_code = dlg.exec_()
        if return_code == 0:
            value = dlg.get_value()
            if value["function"] == "delete":
                self.portfolio.delete_company(name)
                self.portfolio.full_update()
                self.list_model.removeRow(index.row())
                self.update_table()

            elif value["function"] == "update":
                item.setText(f'Name: {name}\nNumber: {str(value["number"])}')
                self.portfolio.update_item(name, value["number"])
                self.portfolio.full_update()
                self.update_table()
