# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTime
#import memo_widget
from popup import Popup
import datetime
import memo_db
from User_info import User_Notice   

class Alarm_Memo(QWidget, QtCore.QObject, User_Notice):
    new_signal = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        QWidget.__init__(self, parent = parent)

        self.frame = QtWidgets.QWidget(self)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(30,10,530,440))
        self.frame.setStyleSheet("background-color: #C6FCA9; color: white; border-style: outset; border-radius: 10px; border-color: #AAAAAA; border-width: 2px")

        self.title_input = QtWidgets.QLineEdit(self)
        self.title_input.setGeometry(QtCore.QRect(45,20, 500, 30))
        self.title_input.setStyleSheet("background-color: #FFFFFF; color: black;border-style: outset; border-radius: 5px; border-color: black; border-width: 1px")
        self.title_input.setPlaceholderText("제목")

        self.content_input = QtWidgets.QTextEdit(self)
        self.content_input.setGeometry(QtCore.QRect(45,60, 195, 330))
        self.content_input.setStyleSheet("background-color: #FFFFFF; color: black;border-style: outset; border-radius: 5px; border-color: black; border-width: 1px")
        self.content_input.setPlaceholderText("메모 내용")

        self.date_input = QtWidgets.QCalendarWidget(self)
        self.date_input.setGeometry(QtCore.QRect(260,60, 285, 270))
        self.date_input.setStyleSheet("QToolButton {color: rgb(0, 0, 0);};border-style: outset; border-radius: 5px; border-color: #AAAAAA; border-width: 1px")
        self.date_input.setGridVisible(True)
        self.date_input.setNavigationBarVisible(True)


        self.time = QTime()
        self.current_time = self.time.currentTime()
        self.str_time = self.current_time.toString()

        self.time_input = QtWidgets.QTimeEdit(self.time, self)
        self.time_input.setGeometry(QtCore.QRect(360,340, 100, 30))
        self.time_input.setStyleSheet("background-color: #FFFFFF; color: black;border-style: outset; border-radius: 5px; border-color: white; border-width: 1px")

        set_time = datetime.datetime.now()  #현재시간 겟
        hh = int(str(set_time)[11:13])      #hh
        mm = int(str(set_time)[14:16])      #mm

        self.time_input.setTime(QTime(hh,mm))
        
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
        date = self.get_date()
        time = self.get_time()
        memo_type = 1
        
        flag = self.title_null_check(title)

        if flag:
            flag = self.text_count(content)
            if flag:
                user_name = User_Notice.get_id()
                memo_db.write_memo(user_name, memo_type, title, content, date, time)

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
        
        #서버 용량검사, 메모 글자수 검사

        

    def get_title(self):
        title = self.title_input.text()
        #print("제목: {}".format(title))
        return title

    def get_content(self):
        content = self.content_input.toPlainText()
        #print("내용: {}".format(content))
        return content

    def get_date(self):
        date = self.date_input.selectedDate().toString("yyyy-MM-dd")
        #print("날짜: {}".format(date))
        return date

    def get_time(self):
        time = self.time_input.time().toString("hh:mm")
        #print("시간: {}".format(time))
        return time

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

