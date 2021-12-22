from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, headers):
        super(TableModel, self).__init__()

        self.horizontalHeaders = [''] * len(headers)
        self.verticalHeaders = [''] * 2

        for i, header in enumerate(headers):
            self.setHeaderData(i, Qt.Horizontal, header)
        self._data = data
        self.green = QColor(79, 205, 197)
        self.yellow = QColor(255, 182, 72)
        self.red = QColor(226, 83, 83)
        self.column_color_info = [
            [[0.4, 0.6], [self.red, self.yellow, self.green]],
            [[1.5, 2.0], [self.green, self.yellow, self.red]],
            [[-0.2, 0.5], [self.red, self.yellow, self.green]],
            [[0.6, 1], [self.red, self.yellow, self.green]],
            [[0.1, 0.2], [self.red, self.yellow, self.green]]
        ]

    def setHeaderData(self, section, orientation, data, role=Qt.EditRole):
        if orientation == Qt.Horizontal and role in (Qt.DisplayRole, Qt.EditRole):
            try:
                self.horizontalHeaders[section] = data
                return True
            except:
                return False
        elif orientation == Qt.Vertical and role in (Qt.DisplayRole, Qt.EditRole):
            try:
                self.verticalHeaders[section] = data
                return True
            except:
                return False
        return super().setHeaderData(section, orientation, data, role)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            try:
                return self.horizontalHeaders[section]
            except:
                pass
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            try:
                return self.verticalHeaders[section]
            except:
                pass
        return super().headerData(section, orientation, role)

    def data(self, index, role):
        value = self._data[index.row()][index.column()]
        if role == Qt.DisplayRole:
            if value is None:
                return '--'
            if isinstance(value, float):
                return "%.4f" % value
            if isinstance(value, str):
                return '"%s"' % value
        elif role == Qt.BackgroundRole:
            if isinstance(value, float):
                return self.pick_color(index.column(), value)

    def pick_color(self, column, value):
        for i in range(len(self.column_color_info[column][0])):
            if self.column_color_info[column][0][i] >= value:
                return self.column_color_info[column][1][i]
        return self.column_color_info[column][1][-1]

    def set_data(self, coeffs):
        self._data.clear()
        self.verticalHeaders = [''] * len(coeffs)
        for y, d in enumerate(coeffs):
            l1 = []
            for x, val in enumerate(d.values()):
                l1.append(val)
            self.setHeaderData(y, Qt.Vertical, l1[0])
            self._data.append(l1[2:])
        self.sort(0, QtCore.Qt.AscendingOrder)
        self.layoutChanged.emit()

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        try:
            return len(self._data[0])
        except IndexError:
            return 0
