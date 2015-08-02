# This Python file uses the following encoding: utf-8

from flask import Flask, request, redirect
import twilio.twiml
from tropo import Tropo, Session
from sender import sendToClient

app = Flask(__name__)

@app.route('/', methods=['POST'], defaults={'path': ''})
@app.route('/<path:path>', methods=['POST'])
def handleText(path):
    if request.values.get('Body'):
        print "Recieved Twillio"
        sendToClient(str(path), request.values.get('Body'))
    elif Session(request.values.get('Body')).initialText:
        print "Recieved Troppo"
        sendToClient(str(path), str(request.values.get('Body')).initialText))
    else:
        print "Recieved a message, but it seemed to be empty 😳"
        sendToClient(str(path), "Recieved a message, but it seemed to be empty 😳")
    return 'ayy'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
