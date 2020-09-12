# -*- coding: utf-8 -*-
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPoint

class View_Memo(QWidget):
    #general_signal = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super().__init__()
        self.resize(350, 350)
        self.setMinimumSize(QtCore.QSize(350, 350))
        self.setMaximumSize(QtCore.QSize(350, 350))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: #EAFFDB")
        self.center()

        self.title = QLineEdit(self)
        self.title.setReadOnly(True)
        self.title.setGeometry(QtCore.QRect(15,30,320, 30))
        self.title.setStyleSheet("background-color: #135100;  color: white; border-style: outset; border-radius: 5px; border-width: 2px")
        title_font = self.title.font()
        title_font.setPointSize(16)
        self.title.setFont(title_font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)

        self.memo_window = QTextEdit(self)
        self.memo_window.setReadOnly(True)
        self.memo_window.setGeometry(QtCore.QRect(10,70,330, 280))
        self.memo_window.setStyleSheet("border-style: outset; border-width: 0px")
        memo_font = self.memo_window.font()
        memo_font.setPointSize(11)
        self.memo_window.setFont(memo_font)
        self.memo_window.setReadOnly(True)

        self.close_btn = QtWidgets.QPushButton(self)
        self.close_btn.setGeometry(QtCore.QRect(320,10,20,20))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.getcwd()+'/img/close_btn.PNG'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_btn.setIcon(icon)

        self.close_btn.clicked.connect(lambda: self.close())
        
    def center(self):
        move = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        move.moveCenter(cp)
        self.move(move.topLeft())

    def memo_content(self,content):
        self.memo_window.setText(content)

    def memo_title(self, titlee):
        self.title.setText(titlee)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def close(self):
        #self.general_signal.emit()
        self.deleteLater()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Member_widget()
    #Form.show()
    sys.exit(app.exec_())

