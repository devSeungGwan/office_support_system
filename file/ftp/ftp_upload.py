#-*- encoding: UTF-8 -*-

import ftplib
import os


def file_upload(filename, filepath, server_file_name):
    ftp = ftplib.FTP()
    ftp.encoding='utf-8'

    ip = "52.78.146.225"
    port = 21

    #filepath = ""
    #print("filepath: "+filepath)       #올릴 파일 경로
    login_id = 'yeonwoo'
    login_pwd = '1234'

    ftp.set_pasv(False)

    ftp.connect(ip, port)    #Ftp 주소 Connect(주소 , 포트)

    ftp.login(login_id, login_pwd)         #login (ID, Password)

    ftp.cwd("/home/yeonwoo")   #파일 전송할 Ftp 주소 (받을 주소)

    default_path = os.path.dirname(os.path.realpath('__file__'))

    os.chdir(filepath) #파일 전송 대상의 주소(보내는 주소)
    print("뿌직:",filepath)
    print("응가:",filename)
    myfile = open(filename, 'rb')       #Open( ~ ,'r') <= Text파일은 됨, Open( ~ ,'rb') <= 이미지파일 됨
    ftp.storbinary('STOR ' + server_file_name, myfile)

    os.chdir(default_path)
    myfile.close()  
    ftp.close() 