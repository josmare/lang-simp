from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello_mundo():
    return 'Que onda, banda.'