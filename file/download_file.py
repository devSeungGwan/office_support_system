# -*- coding:utf-8 -*-

from PyQt5.QtWidgets import QMessageBox, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import ftp_download
import file_widget
import file_db

class Download_File(QLineEdit):
    download_signal = QtCore.pyqtSignal()
    fail_not_exist_signal = QtCore.pyqtSignal()
    def __init__(self, parent):
        super(Download_File, self).__init__(parent)
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

        if file_db.file_check(file_widget.prime_number): #고유번호 파일 매칭

            DB_file_path, DB_file_name = file_db.get_file_name_path(file_widget.prime_number)
            print("경로: ",DB_file_path)
            print("네임: ", DB_file_name)
            ftp_download.file_download(DB_file_name, DB_file_path)
            self.download_signal.emit()
            self.cancle()
        else:
            self.fail_not_exist_signal.emit()

    def cancle(self):
        self.deleteLater()