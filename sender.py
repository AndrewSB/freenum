import requests
from flask import Flask

def sendMessage(reciever, content):
    payload = {'number': reciever, 'message': content}
    print 'Sending message to ' + str(reciever) + ' with content ' + str(content)
    return requests.post('http://textbelt.com/text', data=payload)
