import requests
import smtplib
from flask import Flask


def sendMessage(reciever, content):
    payload = {'number': reciever, 'message': content}
    print 'Sending message to ' + str(reciever) + ' with content ' + str(content)
    return requests.post('http://textbelt.com/text', data=payload)

def sendEmail(address, content):
    # Import smtplib for the actual sending function


    # Import the email modules we'll need
    from email.mime.text import MIMEMultipart
    msg = MIMEMultipart()
    # me == the sender's email address
    # you == the recipient's email address
    me = "freenum@freenum.com"
    msg['Subject'] = 'Forwarded text '
    msg['From'] = me
    msg['To'] = address
    msg.attach(MIMEText(content, 'plain'))

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP('localhost')

    s.sendmail(me, [address], msg.as_string())
    s.quit()