#!/usr/bin/env python3
"""parameterise templates"""

import pytz
from flask import Flask, g, render_template, request
from flask_babel import Babel


class Config:
    """config"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """get user"""
    login_id = request.args.get("login_as")
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """get user before any other request fired"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """determine the best match with our supported languages"""
    locale = request.args.get("locale", "")
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user["locale"] in app.config["LANGUAGES"]:
        return g.user["locale"]
    locale_header = request.headers.get("locale", "")
    if locale_header in app.config["LANGUAGES"]:
        return locale_header
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone() -> str:
    """get timezone"""
    timezone = request.args.get("timezone", "").strip()
    if not timezone and g.user:
        timezone = g.user["timezone"]
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config["BABEL_DEFAULT_TIMEZONE"]


@app.route("/")
def index():
    """index / home route"""
    return render_template("7-index.html")
