import smtplib
from email.mime.text import MIMEText


def smtp_id(e_mail:str, search_id):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()  # say Hello
    smtp.starttls()  # TLS 사용시 필요
    smtp.login('songwillson80@gmail.com', 'root1234!@')


    title = 'OSS 아이디 문의 결과'
    text = '사용자님의 아이디는 <' + str(search_id) + '> 입니다.'

    msg = MIMEText(text)               #내용
    msg['Subject'] = title              #제목

    msg['To'] = e_mail
    smtp.sendmail('songwillson80@gmail.com', e_mail, msg.as_string())

    smtp.quit()


def smtp_pwd(e_mail, certify_code):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()  # say Hello
    smtp.starttls()  # TLS 사용시 필요
    smtp.login('songwillson80@gmail.com', 'root1234!@')

    title = 'OSS 인증 코드'

    text = '인증 코드는 <' + certify_code + '> 입니다. \n알맞게 입력해주세요.'

    msg = MIMEText(text)               #내용
    msg['Subject'] = title              #제목

    msg['To'] = e_mail
    smtp.sendmail('songwillson80@gmail.com', e_mail, msg.as_string())

    smtp.quit()