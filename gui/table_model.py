from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data[index.row()][index.column()]
            if value is None:
                # Render time to YYY-MM-DD.
                return '--'

            if isinstance(value, float):
                # Render float to 2 dp
                return "%.2f" % value

            if isinstance(value, str):
                # Render strings with quotes
                return '"%s"' % value

    def set_data(self, coeffs):
        self._data.clear()
        for y, d in enumerate(coeffs.values()):
            l1 = []
            for x, val in enumerate(d.values()):
                if val is float:
                    l1.append(val)
                else:
                    l1.append(val)
            self._data.append(l1[2:])
        self.layoutChanged.emit()

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])
