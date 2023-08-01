#!/usr/bin/env python3
"""Basic Flask App"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """config"""

    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def index():
    """index / home route"""
    return render_template("1-index.html")
