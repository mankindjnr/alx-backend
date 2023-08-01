#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for, g
from flask_babel import Babel, _
"""
i18n tasks with flask and python
"""


app = Flask(__name__)


class Config(object):
    """Config class for Babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """Get locale language"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return app.config['BABEL_DEFAULT_LOCALE']


def get_user(user_id):
    """Get user"""
    if user_id and int(user_id) in users:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """Before request"""
    user_id = request.args.get('login_as')
    g.user = get_user(user_id)


@app.route('/')
def index():
    """Display Hello HBNB!"""
    u_id = request.args.get('login_as')
    user = get_user(u_id)
    return render_template('5-index.html', user=user)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
