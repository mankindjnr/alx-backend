#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
from flask_babel import Babel, _
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


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Get locale language"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index():
    """Display Hello HBNB!"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
