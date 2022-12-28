import sys
from PySide6 import QtCore, QtWidgets
from guitest import Ui_Form

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

# app logic
qfiledialog = QtWidgets.QFileDialog()
fname = qfiledialog.getOpenFileName(ui.label, 'Open file', '/ home')
print(fname)

# run app

sys.exit(app.exec())

