# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
#import memo_widget
from popup import Popup
import memo_db
from User_info import User_Notice

class General_Memo(QWidget, QtCore.QObject, User_Notice):
    new_signal = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        QWidget.__init__(self, parent = parent)
        #super().__init__()
        self.frame = QtWidgets.QWidget(self)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(30,10,530,440))
        self.frame.setStyleSheet("background-color: #C6FCA9; color: white; border-style: outset; border-radius: 10px; border-color: #AAAAAA; border-width: 2px")

        self.title_input = QtWidgets.QLineEdit(self)
        self.title_input.setGeometry(QtCore.QRect(45,20, 500, 30))
        self.title_input.setStyleSheet("background-color: #FFFFFF; color: black;border-style: outset; border-radius: 5px; border-color: black; border-width: 1px")
        self.title_input.setPlaceholderText("제목")

        self.content_input = QtWidgets.QTextEdit(self)
        self.content_input.setGeometry(QtCore.QRect(45,60, 500, 330))
        self.content_input.setStyleSheet("background-color: #FFFFFF; color: black;border-style: outset; border-radius: 5px; border-color: black; border-width: 1px")
        self.content_input.setPlaceholderText("메모 내용")

        self.confirm_btn = QtWidgets.QPushButton(self)
        self.confirm_btn.setGeometry(QtCore.QRect(340, 400, 80, 40))
        self.confirm_btn.setStyleSheet("background-color: #6EF922; color: black; border-style: outset; border-radius: 10px; border-color: #AAAAAA; border-width: 1px")

        self.cancle_btn = QtWidgets.QPushButton(self)
        self.cancle_btn.setGeometry(QtCore.QRect(440, 400, 80, 40))
        self.cancle_btn.setStyleSheet("background-color: #6EF922; color: black; border-style: outset; border-radius: 10px; border-color: #AAAAAA; border-width: 1px")

        self.confirm_btn.clicked.connect(lambda: self.confirm())
        self.cancle_btn.clicked.connect(lambda: self.cancle())

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.confirm_btn.setText(_translate("Form", "확인"))
        self.cancle_btn.setText(_translate("Form", "취소"))

    def confirm(self):
        title = self.get_title()
        content = self.get_content()
        date = '0000-00-00'
        time = '00-00'
        memo_type = 0

        #서버 용량검사, 메모 글자수 검사
        flag = self.title_null_check(title)

        if flag:
            flag = self.text_count(content)
            if flag:
                user_name = User_Notice.get_id()
                memo_db.write_memo(user_name, memo_type, title, content, date, time)
                #아이디 해야함 ㅇㅇ 연동 ㅇㅇ
                #memo_widget.memo_count += 1
                self.popup = Popup(self)
                self.popup.memo_create_complete()
                self.popup.show()
                self.popup.new_signal.connect(self.complete)
            else:
                self.popup = Popup(self)
                self.popup.memo_create_fail_countover()
                self.popup.show()
        else:
            self.popup = Popup(self)
            self.popup.memo_title_null()
            self.popup.show()

        
        
    def get_title(self):
        title = self.title_input.text()
        return title

    def get_content(self):
        content = self.content_input.toPlainText()
        return content
    
    def title_null_check(self, title):
        flag = False
        if title !='':
            flag = True
        return flag

    def text_count(self, text):
        flag = False
        if len(text) <= 200:
            flag = True
        return flag

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

