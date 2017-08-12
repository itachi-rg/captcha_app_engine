import logging

from flask import Flask
from flask import request
from flask_cors import CORS
import requests

app = Flask(__name__)

CORS(app, headers=['Content-Type'])

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/predict', methods=['POST'])
def predict():
    jsonData = request.get_json()
    captchaString = jsonData['captchaString']
    uri = 'http://35.196.233.143/predict?captchaString='+captchaString
    captcha = requests.get(uri)
	
    if len(captcha.text) != 4 :
        return ""
    else :
        return captcha.text

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
