# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Popup(QWidget):
    new_signal = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        
        QWidget.__init__(self, parent = parent)

        self.resize(650, 520)
        self.setMinimumSize(QtCore.QSize(650, 520))
        self.setMaximumSize(QtCore.QSize(650, 520))


        self.frame = QtWidgets.QWidget(self)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(160,210,280,190))
        self.frame.setStyleSheet("background-color: #FFFFFF; border-style: outset; border-radius: 5px; border-color: #3A0000; border-width: 3px")

        self.context = QtWidgets.QLabel(self)
        self.context.setGeometry(QtCore.QRect(170, 230, 260, 90))
        self.context.setStyleSheet("background-color: white")
        context_font = self.context.font()
        context_font.setPointSize(12)
        self.context.setFont(context_font)
        self.context.setText("여기가 어디오?\nasdasdasdasdsdd\nasdasdasdasdadsasd")
        self.context.setAlignment(QtCore.Qt.AlignCenter)

        self.close_btn = QtWidgets.QPushButton(self)
        self.close_btn.setGeometry(QtCore.QRect(225,330,150,50))
        self.close_btn.setStyleSheet("background-color: #3A0000; color: white; border-style: outset; border-radius: 18px; border-color: #3A0000; border-width: 1px")
        close_btn_font = self.close_btn.font()
        close_btn_font.setPointSize(16)
        close_btn_font.setBold(True)
        self.close_btn.setFont(close_btn_font)
        self.close_btn.setText("확    인")


        self.close_btn.clicked.connect(lambda: self.close())

    def close(self):
        self.new_signal.emit()
        self.deleteLater()
    
    def login_fail(self):
        self.context.setText("로그인 실패\n\n아이디와 비밀번호를 확인해주세요.")

    def pwd_coincidence_check(self):
        self.context.setText("비밀번호가 일치하지 않습니다.\n\n다시 입력해주세요.")

    def id_valid_check(self):
        self.context.setText("영문자와 숫자만 사용 가능합니다.\n\n다시 입력해주세요.")

    def id_duplication_check(self):
        self.context.setText("아이디가 이미 사용 중입니다.\n\n다시 입력해주세요.")

    def join_complete(self):
        self.context.setText("회원가입 축하드립니다.")

    def id_email_send(self):
        self.context.setText("메일이 발송되었습니다.\n\n메일을 확인해주세요.")

    def id_search_fail(self):
        self.context.setText("올바른 이메일이 아닙니다.")

    def pwd_email_send(self):
        self.context.setText("메일이 발송되었습니다.\n\n메일을 확인해주세요.")

    def pwd_search_fault(self):
        self.context.setText("아이디와 이메일을\n\n확인해주세요.")

    def pwd_certify_success(self):
        self.context.setText("인증 성공")

    def pwd_certify_fail(self):
        self.context.setText("인증 코드를 확인해주세요.")

    def pwd_update_complete(self):
        self.context.setText("비밀번호 재설정 완료")

    def upload_complete(self):
        self.context.setText("업로드 완료")

    def upload_fail(self):
        self.context.setText("업로드 실패")

    def download_complete(self):
        self.context.setText("다운로드 완료")
    
    def download_fail(self):
        self.context.setText("파일이 존재하지 않습니다.")

    

    def rename_complete(self):
        self.context.setText("파일명 변경 완료")

    def rename_fail(self):
        self.context.setText("파일명 변경 실패")

    def rename_fail_not_owner(self):
        self.context.setText("권한이 없습니다.")

    def delete_complete(self):
        self.context.setText("삭제 완료")

    def delete_fail_not_exist(self):
        self.context.setText("삭제 실패")

    def delete_fail_not_owner(self):
        self.context.setText("권한이 없습니다.")











    def memo_title_null(self):
        self.context.setText("제목을 입력해주세요.")

    def memo_create_fail_countover(self):
        self.context.setText("메모는 200자까지만 가능합니다.\n\n확인해주세요.")

    def memo_create_complete(self):
        self.context.setText("메모 생성 완료")

    def weather_complete(self):
        self.context.setText("날씨 설정 완료")

    def weather_fail(self):
        self.context.setText("지역을 확인해주세요.\n\n한글만 가능합니다.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Member_widget()
    #Form.show()
    sys.exit(app.exec_())

