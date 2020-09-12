# -*- coding:utf-8 -*-

from PyQt5.QtWidgets import QMessageBox, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import ftp_delete
import file_widget
import file_db
import os
from User_info import User_Notice 

class Delete_File(QLineEdit, User_Notice):
    delete_signal = QtCore.pyqtSignal()
    fail_not_exist_signal = QtCore.pyqtSignal()
    fail_not_owner_signal = QtCore.pyqtSignal()
    def __init__(self, parent):
        super(Delete_File, self).__init__(parent)
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
        file_widget.prime_number = event.mimeData().text()      #파일 고유번호 

        owner = file_db.get_file_owner(file_widget.prime_number)    #파일 주인 겟

        if owner == User_Notice.get_id():                       #파일 주인 == 현 사용자 허가
            if file_db.file_check(file_widget.prime_number) != None:        #고유번호에 해당되는 파일 있어?
                                                                            #있엉
                DB_file_path, DB_file_name = file_db.get_file_name_path(file_widget.prime_number)

                ftp_delete.file_delete(DB_file_name, DB_file_path)  #서버 파일 삭제
                file_db.delete_file(file_widget.prime_number)       #디비 정보 삭제
                
                self.delete_signal.emit()
                self.cancle()
                
            else:
                self.fail_not_exist_signal.emit()     #삭제 실패 파일 없졍
        else:
            self.fail_not_owner_signal.emit()       #삭제 실패 권한 없졍


    def cancle(self):
        self.deleteLater()