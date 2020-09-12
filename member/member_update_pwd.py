# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from popup import Popup
import member_search_pwd
import hashlib

from DB_info import DB_config
db = DB_config()

class Update_Member_PWD(QWidget):
    update_signal = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        
        QWidget.__init__(self, parent = parent)

        self.resize(650, 520)
        self.setMinimumSize(QtCore.QSize(650, 520))
        self.setMaximumSize(QtCore.QSize(650, 520))

        self.frame = QtWidgets.QWidget(self)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(30,10,530,500))
        self.frame.setStyleSheet("background-color: #00CE7F; color: white;border-style: outset; border-radius: 5px; border-color: #00CE7F; border-width: 1px")

        self.oss = QtWidgets.QLabel(self)
        self.oss.setGeometry(QtCore.QRect(80, 50, 430, 40))
        self.oss.setText("Office Support System")
        self.oss.setStyleSheet("background-color: #00CE7F; color: black")
        oss_font = self.oss.font()
        oss_font.setPointSize(29)
        oss_font.setBold(True)
        self.oss.setFont(oss_font)

        self.title = QtWidgets.QLabel(self)
        self.title.setGeometry(QtCore.QRect(80, 100, 430, 40))
        self.title.setText("패스워드 재설정")
        self.title.setStyleSheet("background-color: #00CE7F; color: black")
        title_font = self.title.font()
        title_font.setPointSize(20)
        title_font.setBold(True)
        self.title.setFont(title_font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)

        self.pwd1_input = QtWidgets.QLineEdit(self)
        self.pwd1_input.setGeometry(QtCore.QRect(150, 250, 300, 40))
        self.pwd1_input.setStyleSheet("background-color: #FFFFFF; color: black;border-style: outset; border-radius: 5px; border-color: #00E5CA; border-width: 1px")
        self.pwd1_input.setPlaceholderText("패스워드") 
        member_font = self.pwd1_input.font()
        member_font.setPointSize(13)
        member_font.setBold(False)
        self.pwd1_input.setFont(member_font)
        self.pwd1_input.setEchoMode(QtWidgets.QLineEdit.Password)

        self.pwd2_input = QtWidgets.QLineEdit(self)
        self.pwd2_input.setGeometry(QtCore.QRect(150, 320, 300, 40))
        self.pwd2_input.setStyleSheet("background-color: #FFFFFF; color: black;border-style: outset; border-radius: 5px; border-color: #00E5CA; border-width: 1px")
        self.pwd2_input.setPlaceholderText("패스워드 확인")
        self.pwd2_input.setFont(member_font)
        self.pwd2_input.setEchoMode(QtWidgets.QLineEdit.Password)

        self.confirm_btn = QPushButton("확인", self)
        self.confirm_btn.setGeometry(QtCore.QRect(150, 390, 300, 40))
        self.confirm_btn.setStyleSheet("background-color: #FFFFFF; color: #717171; border-style: outset; border-radius: 18px; border-color: #00E5CA; border-width: 1px")
        confirm_btn_font = self.confirm_btn.font()
        confirm_btn_font.setPointSize(20)
        confirm_btn_font.setBold(True)
        self.confirm_btn.setFont(confirm_btn_font)

        self.cancle_btn = QPushButton("취소", self)
        self.cancle_btn.setGeometry(QtCore.QRect(480, 450, 50, 40))
        self.cancle_btn.setStyleSheet("background-color: #00CE7F; color: #717171; border-style: outset; border-radius: 18px; border-color: #00CE7F; border-width: 0px")

        self.confirm_btn.clicked.connect(lambda: self.confirm())
        self.cancle_btn.clicked.connect(lambda: self.cancle())

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


    def confirm(self):
        pwd1 = self.pwd1_input.text()
        pwd2 = self.pwd2_input.text()

        flag = self.pwd_check(pwd1, pwd2)

        if flag:
            self.popup = Popup(self)
            self.popup.pwd_update_complete()
            pwd = (hashlib.sha3_256(pwd1.encode())).hexdigest()
            db.pwd_config(member_search_pwd.id, pwd)    

            self.popup.show()
            self.popup.new_signal.connect(self.complete)
    
    def pwd_check(self, pwd1, pwd2):
        flag = False

        if pwd1 == pwd2:
            flag = True
        else:
            self.popup = Popup(self)
            self.popup.pwd_coincidence_check()
            self.popup.show()

        return flag

    def complete(self):
        self.update_signal.emit()
        self.deleteLater()

    def cancle(self):
        self.deleteLater()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Member_widget()
    #Form.show()
    sys.exit(app.exec_())

