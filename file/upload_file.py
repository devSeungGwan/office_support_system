# -*- coding:utf-8 -*-

from PyQt5.QtWidgets import QMessageBox, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import file_widget
import ftp_upload
import file_db
import datetime
import os
from User_info import User_Notice   

class Upload_File(QLineEdit, User_Notice):
    upload_signal = QtCore.pyqtSignal()
    fail_signal = QtCore.pyqtSignal()
    def __init__(self, parent):
        super(Upload_File, self).__init__(parent)
        self.setGeometry(QtCore.QRect(45,20, 500, 370))
        self.setStyleSheet("background: #C4FAFF; border-style: outset; border-radius: 10px; border-color: #AAAAAA; border-width: 2px ")
        self.setDragEnabled(True)
        self.setReadOnly(True)

    def dragEnterEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dropEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            filepath = str(urls[0].path())[1:]
            print(filepath)
            if filepath[-4:].upper() == "HTML" or filepath[-3:].upper() == "WMA" or filepath[-3:].upper() == "MPG" or filepath[-3:].upper() == "GIF" or filepath[-3:].upper() == "CSS" or filepath[-1:].upper() == "C" or filepath[-4:].upper() == "JAVA" or filepath[-2:].upper() == "PY" or filepath[-3:].upper() == "ZIP" or filepath[-3:].upper() == "TXT" or filepath[-3:].upper() == "PNG" or filepath[-3:].upper() == "JPG" or filepath[-3:].upper() == "HWP" or filepath[-4:].upper() == "DOCS" or filepath[-4:].upper() == "PPTX" or filepath[-3:].upper() == "PDF" or filepath[-3:].upper() == "CSV":
                #25mb 넘으면 실패 처리 
                if self.size_check(filepath):
                    user_name = User_Notice.get_id()
                    file_name = self.get_filename(filepath)
                    from_file_path = self.get_filepath(filepath)
                    To_filepath = '/home/yeonwoo/'
                    upload_time = datetime.datetime.now()
                    file_type = self.get_filetype(file_name)
                    
                    server_file_name = file_db.upload_file(user_name, file_name, To_filepath, file_type)
                    ftp_upload.file_upload(file_name, from_file_path, server_file_name)

                    

                    file_widget.file_count += 1

                    self.upload_signal.emit()
                    self.cancle()
                elif self.size_check("/" + filepath):
                    filepath = "/" + filepath
                    user_name = User_Notice.get_id()
                    file_name = self.get_filename(filepath)
                    from_file_path = self.get_filepath(filepath)
                    To_filepath = '/home/yeonwoo/'
                    upload_time = datetime.datetime.now()
                    file_type = self.get_filetype(file_name)

                    server_file_name = file_db.upload_file(user_name, file_name, To_filepath, file_type)

                    ftp_upload.file_upload(file_name, from_file_path, server_file_name)

                    file_widget.file_count += 1

                    self.upload_signal.emit()
                    self.cancle()
                else:
                    self.fail_signal.emit()

            else:
                dialog = QMessageBox()
                dialog.setWindowTitle("에러")
                dialog.setText("{} 파일은 지원하지 않습니다.".format(filepath[-3:]))
                dialog.setIcon(QMessageBox.Warning)
                dialog.exec_()

    def get_filename(self, file_path):
        idx = file_path.rfind("/")
        file_name = file_path[idx+1:]
        return file_name

    def get_filepath(self, file_path):
        idx = file_path.rfind("/")
        filepath = file_path[:idx+1]
        return filepath

    def get_filetype(self, file_name):
        idx_for_type = file_name.rfind('.')
        file_type = file_name[idx_for_type+1:].upper()
        return file_type

    def size_check(self, file_path):
        flag = 0

        try:
            filesize = os.path.getsize(file_path)   #byte
        except Exception as e:
            print("[file size Erro]", e)
            return False

        if filesize > 100000.0:
            filesize = filesize / (1024.0 ** 2) #megabyte
            flag = 1
        
        if flag == 0:
            #print("크기: {} byte".format(filesize))
            return True
        else:
            #print("크기: {:6.2f} Mbyte".format(filesize))
            if filesize >= 25:
                return False
            else:
                return True

    def cancle(self):
        self.deleteLater()