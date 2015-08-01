from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route('/', methods=['POST'], defaults={'path': ''})
@app.route('/<path:path>', methods=['POST'])
def catch_all(path):
    return 'You want path: %s' % path

if __name__ == '__main__':
    app.run()
