#!/usr/bin/python3
<<<<<<< HEAD

"""Script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
=======
"""Starts a flask app
    listens to 0.0.0.0:5000
    
"""
from models import storage
from flask import Flask
from flask import render_template
>>>>>>> 3a1362a3018cf60f12069a747d6902faac1e5f09

app = Flask(__name__)


<<<<<<< HEAD
@app.route('/states_list', strict_slashes=False)
def states():
    """returns list of states"""
    return render_template('7-states_list.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    """closes the current SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======
@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage.
    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
>>>>>>> 3a1362a3018cf60f12069a747d6902faac1e5f09
