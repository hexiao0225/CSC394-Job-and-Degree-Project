import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
import os
def sendMailText(receiver, content, images):
    msg = MIMEMultipart('related')
    msg['Subject'] = Header("Final Result", "utf-8")
    msg['From'] = "username"
    msg['To'] = receiver

    msgAlternative = MIMEMultipart('alternative')
    msg.attach(msgAlternative)
    msgAlternative.attach(MIMEText(content, 'html', 'utf-8'))

    fp = open(images, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<0>')
    msg.attach(msgImage)

    s = smtplib.SMTP( "host_server", "25")
    s.login("username", "password" )
    s.sendmail("username", receiver, msg.as_string())
