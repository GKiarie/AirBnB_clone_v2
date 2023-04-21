#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask


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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
