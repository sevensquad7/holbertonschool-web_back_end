#!/usr/bin/env python3
"""
Welcome Holberton
"""
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    language config
    """
    LANGUAGES = ['en', 'es']


@app.route("/", methods=['GET'])
def helloWorld():
    """
    Hello world
    """
    return render_template('0-index.html')
