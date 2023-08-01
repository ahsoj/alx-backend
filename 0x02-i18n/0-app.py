#!/usr/bin/env python3
"""Basic Flask App"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """index / home route"""
    return render_template("0-index.html")
