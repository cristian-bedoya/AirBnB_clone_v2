#!/usr/bin/python3
""" starts a Flask web application: """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """ Display “Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_():
    """ Display Hbnb """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
