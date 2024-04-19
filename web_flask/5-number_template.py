#!/usr/bin/python3
"""
    a script that starts a Flask web application:
    Your web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
        index (route(/)): display “Hello HBNB!”
    """
    return "Hello HBNB"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    /hbnb: display “HBNB”
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    /c/<text>: display “C ”, followed by the value of the text
        variable (replace underscore _ symbols with a space )
    """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text="is cool"):
    """
    /python/(<text>): display “Python ”, followed by the value of the text
        variable (replace underscore _ symbols with a space )
    The default value of text is “is cool”
    """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    /number/<n>: display “n is a number” only if n is an integer
    """
    return f"{n:d} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
        /number_template/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
