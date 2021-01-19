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


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Returns a string at the /c/<text> route,
    expands the <text> variable"""
    text_1 = text.replace('_', ' ')
    return 'C %s' % text_1


if __name__ == '__main__':
    app.run(host='0.0.0.0')
