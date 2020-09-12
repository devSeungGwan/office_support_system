# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from popup import Popup
from member_update_pwd import Update_Member_PWD
import member_search_pwd

class Certification(QWidget):
    certify_signal = QtCore.pyqtSignal()
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
        self.title.setText("인증")
        self.title.setStyleSheet("background-color: #00CE7F; color: black")
        title_font = self.title.font()
        title_font.setPointSize(20)
        title_font.setBold(True)
        self.title.setFont(title_font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)

        self.certification_label = QtWidgets.QLabel(self)
        self.certification_label.setGeometry(QtCore.QRect(80, 170, 430, 40))
        self.certification_label.setText("인증 코드를 입력해주세요.")
        self.certification_label.setStyleSheet("background-color: #00CE7F; color: black")
        certification_font = self.certification_label.font()
        certification_font.setPointSize(11)
        certification_font.setBold(False)
        self.certification_label.setFont(certification_font)
        self.certification_label.setAlignment(QtCore.Qt.AlignCenter)

        self.certification_input = QtWidgets.QLineEdit(self)
        self.certification_input.setGeometry(QtCore.QRect(150, 250, 300, 40))
        self.certification_input.setStyleSheet("background-color: #FFFFFF; color: black;border-style: outset; border-radius: 5px; border-color: #00E5CA; border-width: 1px")
        self.certification_input.setPlaceholderText("인증 코드") 
        member_font = self.certification_input.font()
        member_font.setPointSize(13)
        member_font.setBold(False)
        self.certification_input.setFont(member_font)

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
        input_code = self.certification_input.text()
        generate_code = self.get_certify_code()
        
        #print("인풋:",input_code)
        #print("인증:", generate_code)
        if input_code == generate_code:    #id와 email에 둘다 일치하는 정보가 있는지 디비 확인
            #True
            self.popup = Popup(self)
            self.popup.pwd_certify_success()
            self.popup.show()
            self.popup.new_signal.connect(self.popup_confirm)

        else:
            self.popup = Popup(self)
            self.popup.pwd_certify_fail()
            self.popup.show()
        
    def popup_confirm(self):
        self.update_member_pwd = Update_Member_PWD(self)
        self.update_member_pwd.show()

        self.update_member_pwd.update_signal.connect(self.complete)

    def get_certify_code(self):
        return member_search_pwd.return_certify_code()

    def complete(self):
        self.certify_signal.emit()
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

