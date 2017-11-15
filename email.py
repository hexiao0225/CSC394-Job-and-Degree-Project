import smtplib
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header

from config import app

def sendMailText(receiver, content, images=None):
    msg = MIMEMultipart('related')
    msg['Subject'] = Header("Final Result", "utf-8")
    msg['From'] = app.config['EMAIL']
    msg['To'] = receiver

    msgAlternative = MIMEMultipart('alternative')
    msg.attach(msgAlternative)
    msgAlternative.attach(MIMEText(content, 'html', 'utf-8'))

    if images:
        fp = open(images, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', '<0>')
        msg.attach(msgImage)

    s = smtplib.SMTP( "host_server", "25")
    s.login(app.config['EMAIL'], app.config['EMAIL_PASSWORD'] )
    s.sendmail(app.config['EMAIL'], receiver, msg.as_string())
