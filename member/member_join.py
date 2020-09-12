# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from popup import Popup

from DB_info import DB_register
db = DB_register()

class Join_Member(QWidget):

    def __init__(self, parent=None):
        
        QWidget.__init__(self, parent = parent)

        self.resize(650, 520)
        self.setMinimumSize(QtCore.QSize(650, 520))
        self.setMaximumSize(QtCore.QSize(650, 520))

        self.frame = QtWidgets.QWidget(self)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(30,10,530,500))
        self.frame.setStyleSheet("background-color: #00E5CA; color: white;border-style: outset; border-radius: 5px; border-color: #00E5CA; border-width: 1px")

        self.oss = QtWidgets.QLabel(self)
        self.oss.setGeometry(QtCore.QRect(80, 50, 430, 40))
        self.oss.setText("Office Support System")
        self.oss.setStyleSheet("background-color: #00E5CA; color: black")
        oss_font = self.oss.font()
        oss_font.setPointSize(29)
        oss_font.setBold(True)
        self.oss.setFont(oss_font)

        self.title = QtWidgets.QLabel(self)
        self.title.setGeometry(QtCore.QRect(80, 100, 430, 40))
        self.title.setText("회원가입")
        self.title.setStyleSheet("background-color: #00E5CA; color: black")
        title_font = self.title.font()
        title_font.setPointSize(20)
        title_font.setBold(True)
        self.title.setFont(title_font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)

        self.id_input = QtWidgets.QLineEdit(self)
        self.id_input.setGeometry(QtCore.QRect(150, 160, 300, 40))
        self.id_input.setStyleSheet("background-color: #FFFFFF; color: black;border-style: outset; border-radius: 5px; border-color: #00E5CA; border-width: 1px")
        self.id_input.setPlaceholderText("아이디") 
        member_font = self.id_input.font()
        member_font.setPointSize(13)
        member_font.setBold(False)
        self.id_input.setFont(member_font)

        self.pwd1_input = QtWidgets.QLineEdit(self)
        self.pwd1_input.setGeometry(QtCore.QRect(150, 230, 300, 40))
        self.pwd1_input.setStyleSheet("background-color: #FFFFFF; color: black;border-style: outset; border-radius: 5px; border-color: #00E5CA; border-width: 1px")
        self.pwd1_input.setPlaceholderText("패스워드")
        self.pwd1_input.setFont(member_font)
        self.pwd1_input.setEchoMode(QtWidgets.QLineEdit.Password)

        self.pwd2_input = QtWidgets.QLineEdit(self)
        self.pwd2_input.setGeometry(QtCore.QRect(150, 300, 300, 40))
        self.pwd2_input.setStyleSheet("background-color: #FFFFFF; color: black;border-style: outset; border-radius: 5px; border-color: #00E5CA; border-width: 1px")
        self.pwd2_input.setPlaceholderText("패스워드 확인")
        self.pwd2_input.setFont(member_font)
        self.pwd2_input.setEchoMode(QtWidgets.QLineEdit.Password)

        self.email_input = QtWidgets.QLineEdit(self)
        self.email_input.setGeometry(QtCore.QRect(150, 370, 300, 40))
        self.email_input.setStyleSheet("background-color: #FFFFFF; color: black;border-style: outset; border-radius: 5px; border-color: #00E5CA; border-width: 1px")
        self.email_input.setPlaceholderText("이메일")
        self.email_input.setFont(member_font)


        self.join_btn = QPushButton("회원가입", self)
        self.join_btn.setGeometry(QtCore.QRect(150, 440, 300, 40))
        self.join_btn.setStyleSheet("background-color: #CCCCCC; color: #717171; border-style: outset; border-radius: 18px; border-color: #00E5CA; border-width: 1px")
        member_btn_font = self.join_btn.font()
        member_btn_font.setPointSize(20)
        member_btn_font.setBold(True)
        self.join_btn.setFont(member_btn_font)

        self.cancle_btn = QPushButton("취소", self)
        self.cancle_btn.setGeometry(QtCore.QRect(480, 450, 50, 40))
        self.cancle_btn.setStyleSheet("background-color: #00E5CA; color: #717171; border-style: outset; border-radius: 18px; border-color: #00E5CA; border-width: 0px")

        self.join_btn.clicked.connect(lambda: self.join())
        self.cancle_btn.clicked.connect(lambda: self.cancle())

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def join(self):
        id = self.id_input.text()
        pwd1 = self.pwd1_input.text()
        pwd2 = self.pwd2_input.text()
        email = self.email_input.text()

        flag = self.id_check(id)

        if flag == True:
            flag = self.pwd_check(pwd1, pwd2)

        if flag == True:

            db.member_register(id, pwd1,email,"nicname")
            #db.show(id)

            self.popup = Popup(self)
            self.popup.join_complete()
            self.popup.show()

            self.popup.new_signal.connect(self.cancle)

    def id_check(self, id):
        flag = False

        if self.id_valid(id): #id 영문자 숫자 검사
            if db.member_id_check(id): # id 중복 검사
                flag = True
            else:
                self.popup = Popup(self)
                self.popup.id_duplication_check()
                self.popup.show()
        else:
            self.popup = Popup(self)
            self.popup.id_valid_check()
            self.popup.show()
        return flag

    def id_valid(self, id):
        con = True
        for i in id:
            if(ord(i) not in range(48,58) and ord(i) not in range(65,91) and ord(i) not in range(97,123)):
                con = False
                break

        return con

    def pwd_check(self, pwd1, pwd2):
        flag = False

        if pwd1 == pwd2:
            flag = True
        else:
            self.popup = Popup(self)
            self.popup.pwd_coincidence_check()
            self.popup.show()
        return flag

    def cancle(self):
        self.deleteLater()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Member_widget()
    #Form.show()
    sys.exit(app.exec_())

