#!/usr/bin/env python3
"""get locale from request"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """config"""

    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """determine the best match with our supported languages"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """index / home route"""
    return render_template("2-index.html")
