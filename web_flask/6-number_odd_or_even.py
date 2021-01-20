#!/usr/bin/python3
""" starts a Flask web application: """
from flask import Flask, render_template
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
    """Returns a string at the //<text> route,
    expands the <text> variable"""
    text_1 = text.replace('_', ' ')
    return 'C %s' % text_1


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text: 'is cool'):
    """Returns a string at the /python/<text> route,
    expands the <text> variable"""
    text_1 = text.replace('_', ' ')
    return 'Python %s' % text_1


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Returns a string at the /number/<int:n> route"""
    return '%i is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_temp(n):
    """Returns a string at the number/<int:n> route,
    display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Returns a string at the number_odd_or_even/<int:n> route,
    display a HTML page only if n is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
