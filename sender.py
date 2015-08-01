import requests
from flask import Flask

def sendMessage(reciever, content):
    payload = {'number': reciever, 'message': content}
    return requests.post('http://textbelt.com/text', data=payload)
