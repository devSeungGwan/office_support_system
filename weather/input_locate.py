# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from popup import Popup

class Input_Location(QWidget, QtCore.QObject):
    new_signal = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        QWidget.__init__(self, parent = parent)

        self.frame = QtWidgets.QWidget(self)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(150,205,300,200))
        self.frame.setStyleSheet("background-color: #E8AA74; color: white; border-style: outset; border-radius: 10px; border-color: #AAAAAA; border-width: 2px")

        self.location_input = QtWidgets.QLineEdit(self)
        self.location_input.setGeometry(QtCore.QRect(160,235, 280, 50))
        self.location_input.setStyleSheet("background-color: #FFFFFF; color: black;border-style: outset; border-radius: 5px; border-color: black; border-width: 1px")
        self.location_input.setPlaceholderText("지역을 입력하세요.")
        location_font = self.location_input.font()
        location_font.setPointSize(20)
        location_font.setBold(True)
        self.location_input.setFont(location_font)
        self.location_input.setAlignment(QtCore.Qt.AlignCenter)
        self.location_input.returnPressed.connect(lambda: self.confirm())


        self.confirm_btn = QtWidgets.QPushButton(self)
        self.confirm_btn.setGeometry(QtCore.QRect(170, 335, 120, 40))
        self.confirm_btn.setStyleSheet("background-color: #E58639; color: black; border-style: outset; border-radius: 10px; border-color: #AAAAAA; border-width: 1px")
        btn_font = self.confirm_btn.font()
        btn_font.setPointSize(18)
        btn_font.setBold(True)
        self.confirm_btn.setFont(btn_font)

        self.cancle_btn = QtWidgets.QPushButton(self)
        self.cancle_btn.setGeometry(QtCore.QRect(310, 335, 120, 40))
        self.cancle_btn.setStyleSheet("background-color: #E58639; color: black; border-style: outset; border-radius: 10px; border-color: #AAAAAA; border-width: 1px")
        self.cancle_btn.setFont(btn_font)
        self.confirm_btn.clicked.connect(lambda: self.confirm())
        self.cancle_btn.clicked.connect(lambda: self.cancle())

        self.location = ''

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.confirm_btn.setText(_translate("Form", "확인"))
        self.cancle_btn.setText(_translate("Form", "취소"))

    def confirm(self):
        self.location = self.get_location()

        self.popup = Popup(self)
        self.popup.weather_complete()
        self.popup.show()
        self.popup.new_signal.connect(self.complete)

    def send_location(self):
        return self.location

    def get_location(self):
        location = self.location_input.text()
        return location

    def complete(self):
        self.new_signal.emit()
        self.deleteLater()

    def cancle(self):
        self.deleteLater()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Memo_widget()
    #Form.show()
    sys.exit(app.exec_())

