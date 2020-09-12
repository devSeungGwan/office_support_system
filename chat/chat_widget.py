# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from ex_client import Chat_Client

from User_info import User_Notice    
from DB_info import DB_object, DB_login, DB_logout 
db = DB_login() 
db_logout = DB_logout() 

class Ui_Chat_widget(QWidget):

    coerce_logout_signal = QtCore.pyqtSignal()

    def chat_init_(self):           #서버 아이피 포트
        self.chatting = Chat_Client('52.78.146.225', 10001, 'Non-Name') #m ##server_ip, server_port, name, 해당위젯
        #self.chatting = Chat_Client('127.0.0.1', 10001, 'Non-Name')     #, self.threadid

        #self.chatting.start()

    def chat_login_connect(self):
        self.chatting.daemon = True
        self.chatting.set_name(User_Notice.get_id())
        #self.chatting.start()

    def __init__(self, parent=None):
        QWidget.__init__(self, parent = parent)

        self.chat_init_()

        self.resize(360, 520)
        self.setMinimumSize(QtCore.QSize(360, 520))
        self.setMaximumSize(QtCore.QSize(360, 520))

        self.line = QtWidgets.QLabel(self)
        self.line.setGeometry(QtCore.QRect(0,0,3,520))
        self.line.setStyleSheet("background-color: #40b7ba")

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(3, 0, 361, 40))
        self.label.setObjectName("label")
        self.label.setText("   채팅창")
        self.label.setStyleSheet("background-color: #40b7ba; color: white")
        label_font = self.label.font()
        label_font.setPointSize(13)
        label_font.setBold(True)
        self.label.setFont(label_font)

        self.chatTextField = QLineEdit(self)
        self.chatTextField.setGeometry(QtCore.QRect(6, 480, 292, 40))
        self.chatTextField.setStyleSheet("border-style: outset; border-radius: 5px; border-color: #AAAAAA; border-width: 2px")
        self.chatTextField.returnPressed.connect(lambda: self.send())

        self.send_btn = QPushButton("전송", self)
        self.send_btn.setGeometry(QtCore.QRect(300, 480, 60,40))
        self.send_btn.setStyleSheet("background-color: #CCCCCC; color: #717171; border-style: outset; border-radius: 5px; border-color: #CCCCCC; border-width: 1px")
        send_btn_font = self.send_btn.font()
        send_btn_font.setPointSize(14)
        send_btn_font.setBold(True)
        self.send_btn.setFont(send_btn_font)
        self.send_btn.clicked.connect(lambda: self.send())
        
        self.chat_window = QTextEdit(self)
        self.chat_window.setReadOnly(True)
        self.chat_window.setGeometry(QtCore.QRect(4,40,355, 436))
        self.chat_window.setStyleSheet("border-style: outset; border-radius: 5px; border-color: #CCCCCC; border-width: 2px")
    
        font = self.chat_window.font()
        font.setPointSize(13)
        self.chat_window.setFont(font)





        self.chatting.new_signal.connect(self.text_update)





        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def send(self):
            text = self.chatTextField.text()
            textFormatted='{:>0}'.format(text)

            self.chatTextField.setText("")
            self.chat_window.append( text )#자신거 추가
            self.chat_window.setAlignment(QtCore.Qt.AlignRight)
        
            self.chatting.get_msg(text) #서버로 전송

    def text_update(self):
        token_data = self.chatting.msg_token()
        self.msg_classify(token_data)

      ##a 
    def msg_classify(self, data):
        if data[0] == '0': #입장메시지 #logout check
            self.name_compare(data)
        elif data[0] == '1':    # 퇴장메시지
            self.msg_align(data[1]+data[2])
        elif data[0] == '2' :   # 일반내용
            self.msg_align(data[1]+": "+data[2])
        else:
            print('[Error] msg_classify ')
   ##a         
    def msg_align(self, _data):
        self.chat_window.append(_data)
        self.chat_window.setAlignment(QtCore.Qt.AlignLeft)

       ##a 
    def name_compare(self, _data):
        tmp_name = _data[1]
        tmp_name = tmp_name[1:-1]
        print(User_Notice.get_id(), tmp_name)
        if User_Notice.get_id() == tmp_name:
            if db.member_switch_state(tmp_name):
                print('접속 유지')
                pass
            else:
                print('로그아웃 시키기')
                db_logout.member_logout(tmp_name)   ##디비종료
                self.coerce_logout_signal.emit()    ##로그인gui실행
                self.chat_close()                   ##퇴장문구
                self.chatting.stop()                ##연결된 채팅 종료
        else:
            self.msg_align(_data[1]+ _data[2])

    ##a
    def chat_close(self):
        try:
           self.chatting.bye_msg() 
           print('chat- logout')
        except:
            print('[Error] chat-close ')
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Chat_widget()
    Form.show()
    sys.exit(app.exec_())

