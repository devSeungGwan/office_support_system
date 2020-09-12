# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.getcwd()+"/file/ftp")

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from upload_file import Upload_File
from download_file import Download_File
from rename_file import Rename_File
from delete_file import Delete_File
from popup import Popup
import file_db

file_count = file_db.count_file()
prime_number = file_db.prime_check()

class Ui_File_widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent = parent)

        self.resize(650, 520)
        self.setMinimumSize(QtCore.QSize(650, 520))
        self.setMaximumSize(QtCore.QSize(650, 520))
        self.display_frame = QtWidgets.QFrame(self)
        self.display_frame.setGeometry(QtCore.QRect(30, 10, 530, 440))
        self.display_frame.setStyleSheet("background-color: white;border-style: outset; border-width: 0px")

        self.gridLayout = QtWidgets.QGridLayout(self.display_frame)
        self.scrollArea = QtWidgets.QScrollArea(self.display_frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(30, 10, 530, 440))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        
        self.extention_dic = {'TXT': os.getcwd()+'/img/TXT.jpg', 'HWP': os.getcwd()+'/img/HWP.jpg', 'PY': os.getcwd()+'/img/PY.jpg', 'DOCS': os.getcwd()+'/img/DOCS.jpg', 'PPTX': os.getcwd()+'/img/PPTX.jpg',
                                'ZIP': os.getcwd()+'/img/zip.jpg', 'JAVA': os.getcwd()+'/img/JAVA.jpg', 'C': os.getcwd()+'/img/C.jpg', 'PDF': os.getcwd()+'/img/PDF.jpg', 'CSV': os.getcwd()+'/img/csv.jpg', 'HTML': os.getcwd()+'/img/html.jpg', 'JPG': os.getcwd()+'/img/jpg.jpg',
                                'PNG': os.getcwd()+'/img/png.jpg', 'WMA': os.getcwd()+'/img/wma.jpg', 'MPG': os.getcwd()+'/img/mpg.jpg', 'GIF': os.getcwd()+'/img/gif.jpg', 'CSS': os.getcwd()+'/img/css.jpg'
                            }


        self.get_file()
        #print(self.file_collect)
        frame_lists = self.create_var_file(file_count, self.file_collect)

        for frame in frame_lists:
            self.display(frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        
        self.upload_file = QtWidgets.QPushButton(self)
        self.upload_file.setGeometry(QtCore.QRect(44, 460, 80,40))
        self.upload_file.setStyleSheet("background-color: #414141; color: white;border-style: outset; border-radius: 5px; border-color: black; border-width: 1px")

        self.download_file = QtWidgets.QPushButton(self)
        self.download_file.setGeometry(QtCore.QRect(185, 460, 80,40))
        self.download_file.setStyleSheet("background-color: #414141; color: white;border-style: outset; border-radius: 5px; border-color: black; border-width: 1px")

        self.rename_file = QtWidgets.QPushButton(self)
        self.rename_file.setGeometry(QtCore.QRect(330, 460, 80,40))
        self.rename_file.setStyleSheet("background-color: #414141; color: white;border-style: outset; border-radius: 5px; border-color: black; border-width: 1px")

        self.delete_file = QtWidgets.QPushButton(self)
        self.delete_file.setGeometry(QtCore.QRect(475, 460, 80,40))
        self.delete_file.setStyleSheet("background-color: #414141; color: white;border-style: outset; border-radius: 5px; border-color: black; border-width: 1px")
        
        self.cancle_upload_btn = QtWidgets.QPushButton(self)
        self.cancle_upload_btn.setGeometry(QtCore.QRect(460, 400, 80, 40))
        self.cancle_upload_btn.setStyleSheet("background-color: #C4FAFF; color: black; border-style: outset; border-radius: 10px; border-color: #AAAAAA; border-width: 2px")
        
        self.cancle_download_btn = QtWidgets.QPushButton(self)
        self.cancle_download_btn.setGeometry(QtCore.QRect(460, 400, 80, 40))
        self.cancle_download_btn.setStyleSheet("background-color: #C4FAFF; color: black; border-style: outset; border-radius: 10px; border-color: #AAAAAA; border-width: 2px")

        self.cancle_rename_btn = QtWidgets.QPushButton(self)
        self.cancle_rename_btn.setGeometry(QtCore.QRect(460, 400, 80, 40))
        self.cancle_rename_btn.setStyleSheet("background-color: #C4FAFF; color: black; border-style: outset; border-radius: 10px; border-color: #AAAAAA; border-width: 2px")

        self.cancle_delete_btn = QtWidgets.QPushButton(self)
        self.cancle_delete_btn.setGeometry(QtCore.QRect(460, 400, 80, 40))
        self.cancle_delete_btn.setStyleSheet("background-color: #C4FAFF; color: black; border-style: outset; border-radius: 10px; border-color: #AAAAAA; border-width: 2px")

        self.cancle_upload_btn.hide()
        self.cancle_download_btn.hide()
        self.cancle_rename_btn.hide()
        self.cancle_delete_btn.hide()

        #버튼 액션
        self.upload_file.clicked.connect(lambda: self.call_upload())
        self.download_file.clicked.connect(lambda: self.call_download())
        self.rename_file.clicked.connect(lambda: self.call_rename())
        self.delete_file.clicked.connect(lambda: self.call_delete())

        self.cancle_upload_btn.clicked.connect(lambda: self.cancle_upload())
        self.cancle_download_btn.clicked.connect(lambda: self.cancle_download())
        self.cancle_rename_btn.clicked.connect(lambda: self.cancle_rename())
        self.cancle_delete_btn.clicked.connect(lambda: self.cancle_delete())

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        self.upload_file.setText(_translate("Form", "업로드"))
        self.download_file.setText(_translate("Form", "다운로드"))
        self.rename_file.setText(_translate("Form", "파일명 변경"))
        self.delete_file.setText(_translate("Form", "삭제"))

        self.cancle_upload_btn.setText(_translate("Form", "취소"))
        self.cancle_download_btn.setText(_translate("Form", "취소"))
        self.cancle_rename_btn.setText(_translate("Form", "취소"))
        self.cancle_delete_btn.setText(_translate("Form", "취소"))

    def create_var_file(self, count, DB_file):
        frame_lists = []
        prime_list = file_db.prime_check()
        for i in range(0,count):
            frame_list = []
            
            file_var = "" + str(prime_list[i])
            zero_var = "zero_var"+str(i)
            first_var = "first_var"+str(i)
            second_var = "second_var"+str(i)
            third_var = "third_var"+str(i)
            fourth_var = "fourth_var"+str(i)

            frame_list.append(file_var)
            frame_list.append(zero_var)
            frame_list.append(first_var)
            frame_list.append(second_var)
            frame_list.append(third_var)
            frame_list.append(fourth_var)
            frame_list.append(DB_file[i])

            frame_lists.append(frame_list)

        return frame_lists

    def display(self, frame_list):
        #print("frame_list: ",frame_list[6], frame_list[6][4])
        
        frame_list[1] = QGroupBox('', self.scrollAreaWidgetContents)
        frame_list[1].setMaximumSize(QtCore.QSize(550,60))
        frame_list[1].setStyleSheet("background-color: white;border-width: 0px")

        Total_layout = QtWidgets.QBoxLayout(QBoxLayout.LeftToRight, frame_list[1])
        Total_layout.setContentsMargins(0,0,100,0)

        Left_layout = QtWidgets.QBoxLayout(QBoxLayout.LeftToRight)
        Left_layout.setSpacing(0)

        Center_layout = QtWidgets.QBoxLayout(QBoxLayout.TopToBottom)
        Center_layout.setContentsMargins(0,0,0,0)
        Center_layout.setSpacing(0)

        Right_layout = QtWidgets.QBoxLayout(QBoxLayout.LeftToRight)
        Right_layout.setSpacing(0)
        
        frame_list[2] = QtWidgets.QPushButton(frame_list[1])           # 확장자 별 이미지 , 디비 필요
        frame_list[2].setGeometry(QtCore.QRect(10, 10, 70, 60))
        frame_list[2].setMinimumSize(QtCore.QSize(70,60))
        frame_list[2].setMaximumSize(QtCore.QSize(70,60))
        frame_list[2].setStyleSheet("border-width: 0px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.extention_dic[frame_list[6][4]]))
        frame_list[2].setIcon(icon)
        frame_list[2].setIconSize(QtCore.QSize(60,50))

        frame_list[3] = QtWidgets.QLabel(frame_list[1])            
        frame_list[3].setStyleSheet("background-color: #EAFDFF; color: black;border-style: outset; border-radius: 5px; border-color: #3aa0d8; border-width: 2px")
        frame_list[3].setGeometry(QtCore.QRect(80, 10, 250, 30))
        frame_list[3].setMinimumSize(QtCore.QSize(250,30))
        frame_list[3].setMaximumSize(QtCore.QSize(250,30))
        title_font = frame_list[3].font()
        title_font.setPointSize(12)
        title_font.setBold(True)
        frame_list[3].setFont(title_font)
        frame_list[3].setText(frame_list[6][2])                     #파일 제목

        frame_list[4] = QtWidgets.QLabel(frame_list[1])            #업로드날짜

        frame_list[4].setText(str(frame_list[6][3]))

        frame_list[4].setGeometry(QtCore.QRect(80, 40, 250, 30))
        frame_list[4].setMinimumSize(QtCore.QSize(250,30))
        frame_list[4].setMaximumSize(QtCore.QSize(250,30))
        frame_list[4].setStyleSheet("background-color: #EAFDFF; color: black;border-style: outset; border-radius: 5px; border-color: #3aa0d8; border-width: 2px")

        frame_list[5] = QtWidgets.QLineEdit(frame_list[1])          #고유번호
        frame_list[5].setText(frame_list[0])
        frame_list[5].setGeometry(QtCore.QRect(340, 10, 60, 60))
        frame_list[5].setMinimumSize(QtCore.QSize(60,60))
        frame_list[5].setMaximumSize(QtCore.QSize(60,60))
        frame_list[5].setStyleSheet("background-color: #EAFDFF; color: black;border-style: outset; border-radius: 5px; border-color: #3aa0d8; border-width: 1px")
        font = frame_list[5].font()
        font.setPointSize(20)
        font.setBold(True)
        frame_list[5].setFont(font)
        frame_list[5].setDragEnabled(True)
        frame_list[5].setReadOnly(True)
        frame_list[5].setAlignment(QtCore.Qt.AlignCenter)
        
        frame_list[2].clicked.connect(lambda: self.info_file())
        
        Left_layout.addWidget(frame_list[2])
        Center_layout.addWidget(frame_list[3])
        Center_layout.addWidget(frame_list[4])
        Right_layout.addWidget(frame_list[5])

        Total_layout.addLayout(Left_layout)
        Total_layout.addLayout(Center_layout)
        Total_layout.addLayout(Right_layout)

        self.verticalLayout.addWidget(frame_list[1])

    def info_file(self):
        #디비서 소유자, 등등의 내용 가져와서 찍어줄
        print("파일정보 ㅇ")

    def display_update(self):
        self.get_file()

        for i in reversed(range(self.verticalLayout.count())): 
            self.verticalLayout.itemAt(i).widget().setParent(None)

        frame_lists = self.create_var_file(file_count, self.file_collect)

        for frame in frame_lists:
            self.display(frame)

        self.display_frame.update()

    def find_child(self):
        child_list_lineedit = self.findChildren(QtWidgets.QLineEdit)
        child_list_groupbox = self.findChildren(QtWidgets.QGroupBox)
        return child_list_lineedit, child_list_groupbox

    def remove_file(self):
        global file_count

        list_lineedit, list_groupbox = self.find_child()

        for i in range(0, file_count):
            result = list_lineedit[i].text()
            if result == prime_number:    #디비에 result(고유번호)에 해당하는 넘 삭제 메소드 필요
                for g in range(0, file_count):
                    child = list_groupbox[g].findChildren(QtWidgets.QLineEdit)
                    if list_lineedit[i] == child[0]:
                        list_groupbox[g].deleteLater()
                        file_count -= 1
    

    def call_upload(self):
        self.upload = Upload_File(self)
        self.upload.show()

        self.upload.upload_signal.connect(self.upload_success)
        self.upload.fail_signal.connect(self.upload_fail)
        self.cancle_upload_btn.show()

    def upload_success(self):
        self.display_update()
        self.cancle_upload()
        
        self.popup = Popup(self)
        self.popup.upload_complete()
        self.popup.show()

    def upload_fail(self):
        self.cancle_upload()
        
        self.popup = Popup(self)
        self.popup.upload_fail()
        self.popup.show()

    def cancle_upload(self):
        self.upload.deleteLater()
        self.cancle_upload_btn.hide()




    def call_download(self):
        self.download = Download_File(self)
        self.download.show()
        
        self.download.download_signal.connect(self.download_success)
        self.download.fail_not_exist_signal.connect(self.download_fail_not_exist)
        
        self.cancle_download_btn.show()

    def download_success(self):
        self.cancle_download()
        
        self.popup = Popup(self)
        self.popup.download_complete()
        self.popup.show()

    def download_fail_not_exist(self):
        self.cancle_download()
        
        self.popup = Popup(self)
        self.popup.download_fail()
        self.popup.show()

    def cancle_download(self):
        self.download.deleteLater()
        self.cancle_download_btn.hide()





    def call_rename(self):
        self.rename = Rename_File(self)
        self.rename.show()

        self.rename.rename_signal.connect(self.rename_success)
        self.rename.fail_error_signal.connect(self.rename_fail)
        self.rename.fail_not_owner_signal.connect(self.rename_fail_not_owner)
        self.cancle_rename_btn.show()

    def rename_success(self):
        self.display_update()
        self.cancle_rename()
        
        self.popup = Popup(self)
        self.popup.rename_complete()
        self.popup.show()
        

    def rename_fail(self):
        self.cancle_rename()
        
        self.popup = Popup(self)
        self.popup.rename_fail()
        self.popup.show()

    def rename_fail_not_owner(self):
        self.cancle_rename()
        
        self.popup = Popup(self)
        self.popup.rename_fail_not_owner()
        self.popup.show()

    def cancle_rename(self):
        self.rename.deleteLater()
        self.cancle_rename_btn.hide()

    def call_delete(self):
        '''
        if (hasattr(self, 'download')):
            self.cancle_download()
        if (hasattr(self, 'upload')):
            self.cancle_upload()
        if (hasattr(self, 'rename')):
            self.cancle_rename()
        '''
        self.delete = Delete_File(self)
        self.delete.show()

        self.delete.delete_signal.connect(self.delete_success)
        self.delete.fail_not_exist_signal.connect(self.delete_fail_not_exist)
        self.delete.fail_not_owner_signal.connect(self.delete_fail_not_owner)
        self.cancle_delete_btn.show()

    def delete_success(self):
        self.remove_file()

        self.cancle_delete()
        
        self.popup = Popup(self)
        self.popup.delete_complete()
        self.popup.show()

    def delete_fail_not_exist(self):
        self.cancle_delete()
        
        self.popup = Popup(self)
        self.popup.delete_fail_not_exist()
        self.popup.show()

    def delete_fail_not_owner(self):
        self.cancle_delete()
        
        self.popup = Popup(self)
        self.popup.delete_fail_not_owner()
        self.popup.show()

    def cancle_delete(self):
        self.delete.deleteLater()
        self.cancle_delete_btn.hide()

    def get_file(self):
        self.file_collect = file_db.view_file()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_File_widget()
    Form.show()
    sys.exit(app.exec_())

