# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from popup import Popup
from certification import Certification
import generate_certify_code

from DB_info import DB_find
db = DB_find()
import OSS_smtp

generate_code = ''
id = ''
class Search_Member_PWD(QWidget):
    close2_signal = QtCore.pyqtSignal()
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
        self.title.setText("비밀번호 찾기")
        self.title.setStyleSheet("background-color: #00CE7F; color: black")
        title_font = self.title.font()
        title_font.setPointSize(20)
        title_font.setBold(True)
        self.title.setFont(title_font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)

        self.email_info = QtWidgets.QLabel(self)
        self.email_info.setGeometry(QtCore.QRect(80, 170, 430, 40))
        self.email_info.setText("아이디와 이메일을 입력해 주세요.\n인증 이메일을 보내드립니다.")
        self.email_info.setStyleSheet("background-color: #00CE7F; color: black")
        email_info_font = self.email_info.font()
        email_info_font.setPointSize(11)
        email_info_font.setBold(False)
        self.email_info.setFont(email_info_font)
        self.email_info.setAlignment(QtCore.Qt.AlignCenter)

        self.id_input = QtWidgets.QLineEdit(self)
        self.id_input.setGeometry(QtCore.QRect(150, 250, 300, 40))
        self.id_input.setStyleSheet("background-color: #FFFFFF; color: black;border-style: outset; border-radius: 5px; border-color: #00E5CA; border-width: 1px")
        self.id_input.setPlaceholderText("아이디") 
        member_font = self.id_input.font()
        member_font.setPointSize(13)
        member_font.setBold(False)
        self.id_input.setFont(member_font)

        self.email_input = QtWidgets.QLineEdit(self)
        self.email_input.setGeometry(QtCore.QRect(150, 320, 300, 40))
        self.email_input.setStyleSheet("background-color: #FFFFFF; color: black;border-style: outset; border-radius: 5px; border-color: #00E5CA; border-width: 1px")
        self.email_input.setPlaceholderText("이메일") 
        self.email_input.setFont(member_font)

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
        global generate_code
        global id
        id = self.id_input.text()
        email = self.email_input.text()

        if db.pwd_search(id, email):    #id와 email에 둘다 일치하는 정보가 있는지 디비 확인
            #True
            self.popup = Popup(self)
            self.popup.pwd_email_send()

            generate_code = generate_certify_code.generate_code()
            OSS_smtp.smtp_pwd(email, generate_code)

            self.popup.show()

            

            self.popup.new_signal.connect(self.popup_confirm)

        else:
            self.popup = Popup(self)
            self.popup.pwd_search_fault()
            self.popup.show()
        
    def popup_confirm(self):
        self.certification_instance = Certification(self)
        self.certification_instance.show()

        self.certification_instance.certify_signal.connect(self.complete)
    
    

    def complete(self):
        self.close2_signal.emit()
        self.deleteLater()

    def cancle(self):
        self.deleteLater()

def return_certify_code():
    return generate_code

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Member_widget()
    #Form.show()
    sys.exit(app.exec_())

