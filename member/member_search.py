# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from member_search_id import Search_Member_ID
from member_search_pwd import Search_Member_PWD

class Search_Member(QWidget):

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
        self.title.setText("회원정보 찾기")
        self.title.setStyleSheet("background-color: #00CE7F; color: black")
        title_font = self.title.font()
        title_font.setPointSize(20)
        title_font.setBold(True)
        self.title.setFont(title_font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)

        self.id_search_btn = QPushButton("아이디 찾기", self)
        self.id_search_btn.setGeometry(QtCore.QRect(140, 220, 300, 50))
        self.id_search_btn.setStyleSheet("background-color: #FFFFFF; color: #717171; border-style: outset; border-radius: 18px; border-color: #00CE7F; border-width: 1px")
        member_btn_font = self.id_search_btn.font()
        member_btn_font.setPointSize(20)
        member_btn_font.setBold(True)
        self.id_search_btn.setFont(member_btn_font)

        self.pwd_search_btn = QPushButton("비밀번호 찾기", self)
        self.pwd_search_btn.setGeometry(QtCore.QRect(140, 310, 300, 50))
        self.pwd_search_btn.setStyleSheet("background-color: #FFFFFF; color: #717171; border-style: outset; border-radius: 18px; border-color: #00CE7F; border-width: 1px")
        self.pwd_search_btn.setFont(member_btn_font)

        self.cancle_btn = QPushButton("취소", self)
        self.cancle_btn.setGeometry(QtCore.QRect(480, 450, 50, 40))
        self.cancle_btn.setStyleSheet("background-color: #00CE7F; color: #717171; border-style: outset; border-radius: 18px; border-color: #00CE7F; border-width: 0px")

        self.id_search_btn.clicked.connect(lambda: self.search_id())
        self.pwd_search_btn.clicked.connect(lambda: self.search_pwd())
        self.cancle_btn.clicked.connect(lambda: self.cancle())

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def search_id(self):
        self.search_member_id = Search_Member_ID(self)
        self.search_member_id.show()

        self.search_member_id.close1_signal.connect(self.cancle)

    def search_pwd(self):
        self.search_member_pwd = Search_Member_PWD(self)
        self.search_member_pwd.show()

        self.search_member_pwd.close2_signal.connect(self.cancle)

    def cancle(self):
        self.deleteLater()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Member_widget()
    #Form.show()
    sys.exit(app.exec_())

