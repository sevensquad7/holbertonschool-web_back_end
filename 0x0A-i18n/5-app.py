#!/usr/bin/env python3
"""
Welcome Holberton
"""
from flask import Flask, render_template, g, request
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    language config
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """
    the best match with our supported languages.
    """
    locale = request.args.get("locale")
    if locale in Config.LANGUAGES:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


app.config.from_object(Config)


def get_user():
    ''' returns user from mocked db '''
    login_as = request.args.get("login_as", False)
    if login_as:
        user = users.get(int(login_as), False)
        if user:
            return user
    return None


@app.before_request
def before_request():
    ''' self descriptive '''
    user = get_user()
    g.user = user


@app.route("/", methods=['GET'])
def helloWorld():
    """
    Hello world
    """
    return render_template('5-index.html')
