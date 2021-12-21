import sys

from PyQt5 import QtWidgets, uic

from gui import MainWindow

import requests_cache

requests_cache.install_cache('requests_cache')

example_portfolio = [{"name": "aapl", "number": 1.0},
                     {"name": "goog", "number": 0.5}]

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
