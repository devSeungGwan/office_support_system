# -*- coding:utf-8 -*-

from PyQt5.QtWidgets import QMessageBox, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import ftp_rename
import file_db
import file_widget
from rename_input import Rename_Input 
from User_info import User_Notice 

class Rename_File(QLineEdit):
    rename_signal = QtCore.pyqtSignal()
    fail_error_signal = QtCore.pyqtSignal()
    fail_not_owner_signal = QtCore.pyqtSignal()

    def __init__(self, parent):
        super(Rename_File, self).__init__(parent)
        self.parent = parent
        self.setGeometry(QtCore.QRect(460,20, 80, 370))
        self.setStyleSheet("background: #C4FAFF; border-style: outset; border-radius: 10px; border-color: #AAAAAA; border-width: 2px ")
        self.setDragEnabled(True)
        self.setReadOnly(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        file_widget.prime_number = event.mimeData().text()

        owner = file_db.get_file_owner(file_widget.prime_number)

        if owner == User_Notice.get_id(): 
            if file_db.file_check(file_widget.prime_number) != None:
                
                #a
                self.info_loading()
                self.call_rename_input()
                self.input_rename.new_signal.connect(self.test)    #rename_input.py 완료신호오면 실행하도록
            else:
                self.fail_error_signal.emit()       #에러
        else:
            self.fail_not_owner_signal.emit()       #권한 없
    
    def info_loading(self):
        self.DB_file_path, self.DB_file_name = file_db.get_file_name_path(file_widget.prime_number)
        ##DB_file_name <-.txt . py ... remove
        extension_idx = self.DB_file_name.rfind('.')
        if extension_idx == -1:
            self.extension = ""
            print('test():', "")
            pass
        else:
            self.extension = self.DB_file_name[extension_idx:]
            print('test():',self.DB_file_name, self.DB_file_path) 

    def call_rename_input(self):
        self.input_rename = Rename_Input(self.parent, self.extension)
        self.input_rename.show()


    def test(self):
        rename = self.input_rename.send_rename()
        rename = rename+self.extension ##확장자추가
        print("asaaaaaaa",rename)

        file_db.rename_file(file_widget.prime_number, rename)
        ftp_rename.file_rename(self.DB_file_name, rename, self.DB_file_path)
        
        self.rename_signal.emit() ##a #file_widget.py<-완료신호
        self.cancle()

    def cancle(self):
        self.deleteLater()