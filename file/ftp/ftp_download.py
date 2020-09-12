#-*- encoding: UTF-8 -*-

import ftplib
import os


def file_download(filename, filepath):
    ftp = ftplib.FTP()
    ftp.encoding='utf-8'

    ip = '52.78.146.225'
    port = 21

    login_id = "yeonwoo"
    login_pwd = '1234'

    ftp.set_pasv(False)
    ftp.connect(ip, port)
    ftp.login(login_id, login_pwd)

    ftp.cwd(filepath)
    
    fd = open("./" + filename,'wb')         
    

    ftp.retrbinary("RETR " + filename, fd.write)

    fd.close()
    ftp.close()