#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Ftn that returns Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """Ftn that returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def url_join(text):
    """Ftn that adds variable sections to a URL"""
    text = text.replace("_", " ")
    return "C " + text


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def url_join_python(text='is cool'):
    """Ftn that adds variable sections to a URL"""
    text = text.replace("_", " ")
    return "Python " + text


@app.route('/number/<int:n>', strict_slashes=False)
def extract_int(n):
    """Ftn that returns number passed if its an integer"""
    if type(int(n)) == int:
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_page(n=None):
    """Ftn that returns number passed if its an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_page_even_odd(n=None):
    """Ftn that returns number passed if its an integer"""
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
