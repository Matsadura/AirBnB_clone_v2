#!/usr/bin/python3
""" Starts a Flask Web Application """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

tmp = storage.all(State)
states = tmp.values()


@app.teardown_appcontext
def remove_sqlsession(tmp):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
