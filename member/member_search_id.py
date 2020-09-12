# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from popup import Popup

from DB_info import DB_find
db = DB_find()
import OSS_smtp

class Search_Member_ID(QWidget):
    close1_signal = QtCore.pyqtSignal()
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
        self.title.setText("아이디 찾기")
        self.title.setStyleSheet("background-color: #00CE7F; color: black")
        title_font = self.title.font()
        title_font.setPointSize(20)
        title_font.setBold(True)
        self.title.setFont(title_font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)

        self.email_info = QtWidgets.QLabel(self)
        self.email_info.setGeometry(QtCore.QRect(80, 170, 430, 40))
        self.email_info.setText("가입시 등록하신 이메일 주소를 입력해 주세요.\n아이디가 포함된 이메일을 보내드립니다.")
        self.email_info.setStyleSheet("background-color: #00CE7F; color: black")
        email_info_font = self.email_info.font()
        email_info_font.setPointSize(11)
        email_info_font.setBold(False)
        self.email_info.setFont(email_info_font)
        self.email_info.setAlignment(QtCore.Qt.AlignCenter)

        self.email_input = QtWidgets.QLineEdit(self)
        self.email_input.setGeometry(QtCore.QRect(150, 250, 300, 40))
        self.email_input.setStyleSheet("background-color: #FFFFFF; color: black;border-style: outset; border-radius: 5px; border-color: #00E5CA; border-width: 1px")
        self.email_input.setPlaceholderText("이메일") 
        member_font = self.email_input.font()
        member_font.setPointSize(13)
        member_font.setBold(False)
        self.email_input.setFont(member_font)

        self.email_btn = QPushButton("확인", self)
        self.email_btn.setGeometry(QtCore.QRect(150, 370, 300, 40))
        self.email_btn.setStyleSheet("background-color: #FFFFFF; color: #717171; border-style: outset; border-radius: 18px; border-color: #00E5CA; border-width: 1px")
        email_btn_font = self.email_btn.font()
        email_btn_font.setPointSize(20)
        email_btn_font.setBold(True)
        self.email_btn.setFont(email_btn_font)

        self.cancle_btn = QPushButton("취소", self)
        self.cancle_btn.setGeometry(QtCore.QRect(480, 450, 50, 40))
        self.cancle_btn.setStyleSheet("background-color: #00CE7F; color: #717171; border-style: outset; border-radius: 18px; border-color: #00CE7F; border-width: 0px")

        self.email_btn.clicked.connect(lambda: self.confirm())
        self.cancle_btn.clicked.connect(lambda: self.cancle())

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


    def confirm(self):
        email = self.email_input.text()

        #email로 아이디 전송 ㅇ 과정 필요 

        self.popup = Popup(self)

        search_id = db.id_search(email) 
        
        if search_id == None:
            self.popup.id_search_fail()
            pass
        else:
            self.popup.id_email_send()
            OSS_smtp.smtp_id(email, search_id)
            #비번은 (id, email, "title", "context", )

        self.popup.show()
        self.popup.new_signal.connect(self.popup_confirm)


    def popup_confirm(self):
        self.close1_signal.emit()
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

