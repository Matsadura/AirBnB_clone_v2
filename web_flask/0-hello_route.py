#!/usr/bin/python3
""" Starts a simple Flask Web Application """
from flask import Flask

app = Flask('__name__')


@app.route("/", strict_slashes=False)
def root():
    """ Displays Hello HBNB! """
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host="0.0.0.0")
