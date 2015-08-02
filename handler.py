from flask import Flask, request, redirect
import twilio.twiml
from tropo import Tropo, Session
from sender import sendMessage

app = Flask(__name__)

@app.route('/', methods=['POST'], defaults={'path': ''})
@app.route('/<path:path>', methods=['POST'])
def handleText(path):
    if request.values.get('Body'):
        print "Recieved Twillio"
        sendMessage(str(path), request.values.get('Body'))
    else if Session(request.body).initialText:
        print "Recieved Troppo"
        sendMessage(str(path), str(Session(request.body).initialText))
    else:
        print "Recieved a message, but it seemed to be empty 😳"
        sendMessage(str(path), "Recieved a message, but it seemed to be empty 😳")
    return 'ayy'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
