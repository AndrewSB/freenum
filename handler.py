from flask import Flask, request, redirect
import twilio.twiml
from sender import sendMessage

app = Flask(__name__)

@app.route('/', methods=['POST'], defaults={'path': ''})
@app.route('/<path:path>', methods=['POST'])
def catch_all(path):
    sendMessage('6508155781', str(path))
    return 'You want path: %s' % path

if __name__ == '__main__':
    app.run()
