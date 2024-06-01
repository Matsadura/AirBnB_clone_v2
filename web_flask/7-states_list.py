#!/usr/bin/python3
""" Starts a Flask Web Application """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

tmp = storage.all(State)
states = tmp.values()


@app.teardown_appcontext
def remove_sqlsession(tmp=None):
    storage.close()


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
    if n.isdigit():
        return f"{escape(n)} is a number"
    abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def Number(n):
    """ Displays a HTML page only if n is an integer """
    if n.isdigit():
        return render_template('5-number.html', n=escape(n))
    abort(404)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def number_odd_even(n):
    if n.isdigit():
        return render_template('6-number_odd_or_even.html', n=eval(escape(n)))
    abort(404)


@app.route('/states_list', strict_slashes=False)
def states_list():
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
