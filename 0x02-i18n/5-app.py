#!/usr/bin/env python3
"""parameterise templates"""

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
    queries = request.query_string.decode("utf-8").split("?")[-1]
    query_table = dict(
        map(
            lambda locale: (locale if "=" in locale else "{}=".format(locale)).split(
                "="
            ),
            queries,
        )
    )
    if "locale" in query_table:
        if query_table["locale"] in app.config["LANGUAGES"]:
            return query_table["locale"]
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """index / home route"""
    return render_template("5-index.html")
