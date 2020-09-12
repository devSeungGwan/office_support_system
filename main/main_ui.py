# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.getcwd()+"/member")
sys.path.insert(0, os.getcwd()+"/file")
sys.path.insert(0, os.getcwd()+"/memo")
sys.path.insert(0, os.getcwd()+"/weather")
sys.path.insert(0, os.getcwd()+"/chat")

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import *
from member_widget import Ui_Member_widget
from file_widget import Ui_File_widget
from memo_widget import Ui_Memo_widget
from weather_widget import Ui_Weather_widget
from chat_widget import Ui_Chat_widget
from main_widget import Ui_Main_widget

import time     #a
from User_info import User_Notice    #a
from DB_info import DB_object, DB_logout #a
db = DB_logout() #a

class Ui_MainWindow(User_Notice):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1130, 520)
        MainWindow.setMinimumSize(QtCore.QSize(1130, 520))
        MainWindow.setMaximumSize(QtCore.QSize(1130, 520))
        self.center()
        
        MainWindow.setStyleSheet("background-color: white")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(220, 520))
        self.centralwidget.setObjectName("centralwidget")
        
        self.OSS_logo = QtWidgets.QPushButton(self.centralwidget)
        self.OSS_logo.setGeometry(QtCore.QRect(0, 0, 220, 130))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(os.getcwd()+"/img/OSS2.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OSS_logo.setIcon(icon1)
        self.OSS_logo.setIconSize(QtCore.QSize(220,130))

        self.memo_logo = QtWidgets.QPushButton(self.centralwidget)
        self.memo_logo.setGeometry(QtCore.QRect(0, 260, 220, 130))
        self.memo_logo.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(os.getcwd()+"/img/memo.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.memo_logo.setIcon(icon2)
        self.memo_logo.setIconSize(QtCore.QSize(220, 130))
        self.memo_logo.setFlat(True)


        self.file_logo = QtWidgets.QPushButton(self.centralwidget)
        self.file_logo.setGeometry(QtCore.QRect(0, 130, 220, 130))
        self.file_logo.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(os.getcwd()+"/img/file.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.file_logo.setIcon(icon3)
        self.file_logo.setIconSize(QtCore.QSize(220, 130))
        self.file_logo.setFlat(True)


        self.weather_logo = QtWidgets.QPushButton(self.centralwidget)
        self.weather_logo.setGeometry(QtCore.QRect(0, 390, 220, 130))
        self.weather_logo.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(os.getcwd()+"/img/weather.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.weather_logo.setIcon(icon4)
        self.weather_logo.setIconSize(QtCore.QSize(220, 130))
        self.weather_logo.setFlat(True)


        MainWindow.setCentralWidget(self.centralwidget)

        self.line = QtWidgets.QLabel(self)
        self.line.setGeometry(QtCore.QRect(217,0,3,520))
        self.line.setStyleSheet("background-color: #999999")

        self.childmain = Ui_Main_widget(self)
        self.childmain.setGeometry(QtCore.QRect(200,0,650,520))
        
        '''
        self.childfile = Ui_File_widget(self)
        self.childfile.setGeometry(QtCore.QRect(200,0,650,520))
        
        self.childmemo = Ui_Memo_widget(self)
        self.childmemo.setGeometry(QtCore.QRect(200,0,650,520))

        self.childweather = Ui_Weather_widget(self)
        self.childweather.setGeometry(QtCore.QRect(200,0,650,520))
        '''
        self.childchat = Ui_Chat_widget(self)
        self.childchat.setGeometry(QtCore.QRect(770,0,360,520))


        self.childchat.coerce_logout_signal.connect(self.dis_allow_fuction)
        '''
        self.childfile.hide()
        self.childmemo.hide()
        self.childweather.hide()
        '''
        self.OSS_logo.clicked.connect(lambda: self.main_w())
        self.file_logo.clicked.connect(lambda: self.file_w())
        self.memo_logo.clicked.connect(lambda: self.memo_w())
        self.weather_logo.clicked.connect(lambda: self.weather_w())

        
        self.file_logo.setEnabled(False)
        self.memo_logo.setEnabled(False)
        self.weather_logo.setEnabled(False)
        self.childchat.setEnabled(False)

        self.member = Ui_Member_widget(self)
        self.member.setGeometry(QtCore.QRect(200, 0, 650, 520))
        self.member.login_signal.connect(self.allow_fuction)

        self.close_btn = QtWidgets.QPushButton(self)
        self.close_btn.setGeometry(QtCore.QRect(1100,10,20,20))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.getcwd()+"/img/close_btn.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_btn.setIcon(icon)
        self.close_btn.clicked.connect(lambda: self.closeContext())         #a

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def allow_fuction(self):

        self.childfile = Ui_File_widget(self)
        self.childfile.setGeometry(QtCore.QRect(200,0,650,520))
        
        self.childmemo = Ui_Memo_widget(self)
        self.childmemo.setGeometry(QtCore.QRect(200,0,650,520))

        self.childweather = Ui_Weather_widget(self)
        self.childweather.setGeometry(QtCore.QRect(200,0,650,520))

        self.file_logo.setEnabled(True)
        self.memo_logo.setEnabled(True)
        self.weather_logo.setEnabled(True)
        self.childchat.setEnabled(True)

        self.childfile.hide()
        self.childmemo.hide()
        self.childweather.hide()

        self.childchat.chat_init_()                  #a, 
        self.childchat.chat_login_connect()         #a, chat_widget.py
        self.childchat.chatting.new_signal.connect(self.childchat.text_update)   #a
    
    #a
    def dis_allow_fuction(self):
        self.file_logo.setEnabled(False)
        self.memo_logo.setEnabled(False)
        self.weather_logo.setEnabled(False)
        self.childchat.setEnabled(False)

        QMessageBox.about(None,"logout", "다른 곳에서 로그인되었습니다.") 
        self.member = Ui_Member_widget(self)
        self.member.setGeometry(QtCore.QRect(200, 0, 650, 520))
        self.member.login_signal.connect(self.allow_fuction)
        self.member.show()
    #

    def main_w(self):
        self.childmain.show()
        self.childfile.hide()
        self.childmemo.hide()
        self.childweather.hide()

    def file_w(self):
        self.childfile.show()
        self.childmain.hide()
        self.childmemo.hide()
        self.childweather.hide()

    def memo_w(self):
        self.childfile.hide()
        self.childmain.hide()
        self.childmemo.show()
        self.childweather.hide()

    def weather_w(self):
        self.childfile.hide()
        self.childmain.hide()
        self.childmemo.hide()
        self.childweather.show()

    def center(self):
        move = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        move.moveCenter(cp)
        self.move(move.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
    
    #a
    def closeContext(self):
        ###################chatting 문구, db login_switch=0
        #all connect -> exit
        out_id=User_Notice.get_id()
        
        try:
            if out_id != False:
                self.childchat.chat_close()
                db.member_logout(out_id)
        finally:
            db.mysql_close()
        time.sleep(0.01)

        self.deleteLater()
        self.close()
#

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

