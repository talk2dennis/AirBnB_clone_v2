#!/usr/bin/python3
"""
    a script that starts a Flask web application:
    Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    display "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    display "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    display "C" followed by the text passed as an argurement
    """
    name = text.replace('_', ' ')
    return f"C {name}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
