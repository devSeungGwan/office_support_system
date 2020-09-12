# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from member_join import Join_Member
from member_search import Search_Member
from popup import Popup

from User_info import User_Notice                    
from DB_info import DB_login,DB_logout

db = DB_login()
db_logout = DB_logout()

class Ui_Member_widget(QWidget, QtCore.QObject, User_Notice):
    login_signal = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        
        QWidget.__init__(self, parent = parent)

        self.resize(650, 520)
        self.setMinimumSize(QtCore.QSize(650, 520))
        self.setMaximumSize(QtCore.QSize(650, 520))

        self.frame = QtWidgets.QWidget(self)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(30,10,530,500))
        self.frame.setStyleSheet("background-color: #00E5AC; color: white;border-style: outset; border-radius: 5px; border-color: #00E5AC; border-width: 1px")

        self.oss = QtWidgets.QLabel(self)
        self.oss.setGeometry(QtCore.QRect(80, 50, 430, 40))
        self.oss.setText("Office Support System")
        self.oss.setStyleSheet("background-color: #00E5AC; color: black")
        oss_font = self.oss.font()
        oss_font.setPointSize(29)
        oss_font.setBold(True)
        self.oss.setFont(oss_font)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(80, 100, 430, 40))
        self.label.setText("로그인")
        self.label.setStyleSheet("background-color: #00E5AC; color: black")
        label_font = self.label.font()
        label_font.setPointSize(20)
        label_font.setBold(True)
        self.label.setFont(label_font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.id_input = QtWidgets.QLineEdit(self)
        self.id_input.setGeometry(QtCore.QRect(150,200, 300, 40))
        self.id_input.setStyleSheet("background-color: #FFFFFF; color: black;border-style: outset; border-radius: 5px; border-color: #00E5AC; border-width: 1px")
        self.id_input.setPlaceholderText("아이디") 
        member_font = self.id_input.font()
        member_font.setPointSize(16)
        member_font.setBold(False)
        self.id_input.setFont(member_font)

        self.pwd_input = QtWidgets.QLineEdit(self)
        self.pwd_input.setGeometry(QtCore.QRect(150,270, 300, 40))
        self.pwd_input.setStyleSheet("background-color: #FFFFFF; color: black;border-style: outset; border-radius: 5px; border-color: #00E5AC; border-width: 1px")
        self.pwd_input.setPlaceholderText("패스워드")
        self.pwd_input.setFont(member_font)
        self.pwd_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd_input.returnPressed.connect(lambda: self.login())

        self.login_btn = QPushButton("로그인", self)
        self.login_btn.setGeometry(QtCore.QRect(160, 340, 130, 40))
        self.login_btn.setStyleSheet("background-color: #DDDDDD; color: #717171; border-style: outset; border-radius: 18px; border-color: #00E5AC; border-width: 1px")
        member_btn_font = self.login_btn.font()
        member_btn_font.setPointSize(20)
        member_btn_font.setBold(True)
        self.login_btn.setFont(member_btn_font)

        self.join_btn = QPushButton("회원가입", self)
        self.join_btn.setGeometry(QtCore.QRect(310, 340, 130, 40))
        self.join_btn.setStyleSheet("background-color: #DDDDDD; color: #717171; border-style: outset; border-radius: 18px; border-color: #00E5AC; border-width: 1px")
        self.join_btn.setFont(member_btn_font)

        self.search_btn = QPushButton("회원정보 찾기", self)
        self.search_btn.setGeometry(QtCore.QRect(210, 410, 180, 40))
        self.search_btn.setStyleSheet("background-color: #00E5AC; color: #717171; border-style: outset; border-radius: 18px; border-color: #00E5AC; border-width: 0px")
        search_font = self.search_btn.font()
        search_font.setPointSize(12)
        search_font.setBold(False)
        self.search_btn.setFont(search_font)

        self.login_btn.clicked.connect(lambda: self.login())
        self.join_btn.clicked.connect(lambda: self.join_form())
        self.search_btn.clicked.connect(lambda: self.search_form())

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        
    ##a 
    def login(self):
        id = self.id_input.text()
        pwd = self.pwd_input.text()

        info = db.member_equal(id, pwd)
        if info == False:            #로그인 정보확인 ㅇ
            self.popup = Popup(self)
            self.popup.login_fail()
            self.popup.show()
        else:
            #if db.member_switch_state(id):  #접속중일때 switch->0
            #    db_logout.member_logout(id)
            db.member_login(id)                  #(id, email 반환해줌)
            User_Notice.info_update(info)               ##a 로그인정보 업데이트
            self.login_signal.emit()   
            self.deleteLater()
    ##

    def search_form(self):
        self.search_member = Search_Member(self)
        self.search_member.show()

    def join_form(self):
        self.join_member = Join_Member(self)
        self.join_member.show()

    def join(self):
        print("회원가입")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Member_widget()
    #Form.show()
    sys.exit(app.exec_())

