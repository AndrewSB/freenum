import requests
import smtplib
from flask import Flask
from email.mime.text import MIMEMultipart

def sendToClient(reciever, content):
    if '@' in reciever: # the reciever is an email address
        sendEmail(reciever, content)
    else:
        sendSMS(reciever, content)


def sendSMS(reciever, content):
    payload = {'number': reciever, 'message': content}
    print 'Sending message to ' + str(reciever) + ' with content ' + str(content)
    return requests.post('http://textbelt.com/text', data=payload)

def sendEmail(reciever, content):
    msg = MIMEMultipart()
    msg['Subject'] = str(content)
    msg['From'] = "freenum@freenum.com"
    msg['To'] = reciever
    msg.attach(MIMEText(content, 'plain'))

    s = smtplib.SMTP('localhost')

    s.sendmail("freenum@freenum.com", [reciever], msg.as_string())
    s.quit()
