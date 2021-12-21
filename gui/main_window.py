from PyQt5 import QtWidgets, uic, QtGui, QtCore
from requests import get

from gui.portfolio import Portfolio


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('gui/resources/main_window.ui', self)
        self.portfolio = Portfolio()
        self.init_ui()

    def init_ui(self):
        self.list_model = QtGui.QStandardItemModel()
        self.companies_list.setModel(self.list_model)
        self.submit_button.clicked.connect(self.add_company_from_form)

    def add_company_from_form(self):
        name = self.line_edit.text()
        number = self.doubleSpinBox.value()
        self.portfolio.add_company(name, number)
        it = QtGui.QStandardItem(f"Name: {name}; \nNumber: {str(number)}")
        self.list_model.appendRow(it)
        image = get('https://logo.clearbit.com/apple.com', stream=True)
        image = image.content
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(image)
        pixmap = pixmap.scaledToWidth(64)
        it.setData(pixmap, QtCore.Qt.DecorationRole)
