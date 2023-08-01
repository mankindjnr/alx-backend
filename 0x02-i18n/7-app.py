#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for, g
from flask_babel import Babel, _
import pytz
from babel import dates
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


@babel.timezoneselector
def get_timezone():
    """Get user's preferred time zone"""
    # 1. Find timezone parameter in URL parameters
    timezone = request.args.get('timezone')
    if timezone:
        try:
            # Validate the provided timezone using pytz.timezone
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # 2. Find time zone from user settings (if available)
    user_timezone = get_user_preferred_timezone()
    if user_timezone:
        try:
            # Validate the user's preferred timezone using pytz.timezone
            pytz.timezone(user_timezone)
            return user_timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # 3. Default to UTC (if no valid timezone found)
    return 'UTC'


def get_user_preferred_timezone():
    """user's preferred timezone from user settings"""
    user_timezone = 'America/New_York'
    return user_timezone


@babel.localeselector
def get_locale():
    """Get locale language"""
    # 1. Locale from URL parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # 2. Locale from user settings (if available)
    user_locale = get_user_preferred_locale()
    if user_locale and user_locale in app.config['LANGUAGES']:
        return user_locale

    # 3. Locale from request header (e.g., 'Accept-Language' header)
    header_locale = get_locale_from_request_header()
    if header_locale and header_locale in app.config['LANGUAGES']:
        return header_locale

    # 4. Default locale
    return app.config['BABEL_DEFAULT_LOCALE']


def get_user_preferred_locale():
    """get the user's preferred locale from user settings"""
    user_locale = 'en'
    return user_locale


def get_locale_from_request_header():
    """Function to get the locale from the request header"""
    header_locale = 'en'
    return header_locale


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
    return render_template('7-index.html', user=user)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
