import sys
sys.path.insert(0, "./main")

import main_ui
from PyQt5 import QtCore, QtGui, QtWidgets
from DB_info import DB_object

DB_object.mysql_connect()

class OpenWindow(QtWidgets.QMainWindow, main_ui.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = OpenWindow()
    window.show()
    sys.exit(app.exec_())
