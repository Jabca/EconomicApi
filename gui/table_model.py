from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, headers):
        super(TableModel, self).__init__()

        self.horizontalHeaders = [''] * len(headers)
        self.verticalHeaders = [''] * 2

        for i, header in enumerate(headers):
            self.setHeaderData(i, Qt.Horizontal, header)
        self._data = data

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
        if role == Qt.DisplayRole:
            value = self._data[index.row()][index.column()]
            if value is None:

                return '--'

            if isinstance(value, float):

                return "%.4f" % value

            if isinstance(value, str):

                return '"%s"' % value

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
