from flask import Flask, request, redirect
import twilio.twiml
from sender import sendMessage

app = Flask(__name__)

@app.route('/', methods=['POST'], defaults={'path': ''})
@app.route('/<path:path>', methods=['POST'])
def catch_all(path):
    sendMessage(str(path), request.values.get('Body'))
    return 'ayy'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
