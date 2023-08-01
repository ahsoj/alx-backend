#!/usr/bin/env python3
"""parameterise templates"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """config"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


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
    return render_template("2-index.html")
