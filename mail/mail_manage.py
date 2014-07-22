# coding=utf8

from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

import datetime

from mail.config import MAIL_FROM, MAIL_ACCOUNT, MAIL_SERVER, MAIL_SECRET


def sendMail(address):
    msg = MIMEMultipart()
    att = MIMEText(open('/Users/langley/Desktop/Test/pic1.png', 'rb').read(), 'base64', 'gb2312')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="attach.jpg"'
    msg.attach(att)

    if address == '':
        msg['to'] = '295046974@qq.com'
    else:
        msg['to'] = str(address)

    msg['from'] = MAIL_FROM
    msg['subject'] = Header('testMail (' + str(datetime.date.today()) + ')', 'gb2312')

    server = smtplib.SMTP(MAIL_SERVER)
    server.login(MAIL_ACCOUNT, MAIL_SECRET)
    error = server.sendmail(msg['from'], msg['to'], msg.as_string())
    server.close()
    print(error)
    return error

