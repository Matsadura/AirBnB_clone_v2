#!/usr/bin/python3
""" Starts a Flask Web Application """
from flask import Flask, abort
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root():
    """ Displays Hello HBNB """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Displays HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


@app.route("/number/<n>", strict_slashes=False)
def is_number(n):
    """ Displays 'n is number' only if n is an integer """
    if type(eval(escape(n))) is int:
        return f"{escape(n)} is a number"
    abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
