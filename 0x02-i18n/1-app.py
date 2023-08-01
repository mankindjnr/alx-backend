#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
from flask_babel import Babel
"""
i18n tasks with flask and python
"""


app = Flask(__name__)


babel = Babel(app)


class Config(object):
    """Config class for Babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

@app.route('/')
def index():
    """Display Hello HBNB!"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)