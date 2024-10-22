from flask import Flask
app = Flask(__name__)

@calendar.route('/')
def hello_world():
    return 'Hello, World!'
