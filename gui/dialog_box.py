from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog


class EditDialog(QDialog):
    def __init__(self, name, number):
        super(QDialog, self).__init__()
        uic.loadUi('gui/resources/dialog_edit.ui', self)

        self.first_num = number
        self.data = {"function": "close", "number": number}

        self.company_name.setText(name)
        self.number_box.setValue(number)

        self.apply_button.clicked.connect(self.on_apply)
        self.close_button.clicked.connect(self.on_close)
        self.delete_button.clicked.connect(self.on_delete)

    def on_apply(self):
        self.close()
        self.data["function"] = "update"
        self.data["number"] = self.number_box.value()

    def on_close(self):
        self.close()
        self.data["function"] = "close"
        self.data["number"] = self.first_num

    def on_delete(self):
        self.close()
        self.data["function"] = "delete"
        self.data["delete"] = True

    def get_value(self):
        return self.data


