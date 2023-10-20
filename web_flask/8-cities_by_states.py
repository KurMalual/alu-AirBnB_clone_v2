#!/usr/bin/python3
<<<<<<< HEAD

"""Script that starts a Flask web apllication"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """loads all cities of a State"""

    return render_template('8-cities_by_states.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    """closes the current SQLAlchemy Session"""
=======
"""
    python script that starts a Flask web application
"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states')
def states_list():
    """
        Return: HTML page with list of states
    """
    path = '8-cities_by_states.html'
    states = storage.all(State)
    return render_template(path, states=states)


@app.teardown_appcontext
def app_teardown(arg=None):
    """
        Clean-up session
    """
>>>>>>> 3a1362a3018cf60f12069a747d6902faac1e5f09
    storage.close()


if __name__ == '__main__':
<<<<<<< HEAD
=======
    app.url_map.strict_slashes = False
>>>>>>> 3a1362a3018cf60f12069a747d6902faac1e5f09
    app.run(host='0.0.0.0', port=5000)
