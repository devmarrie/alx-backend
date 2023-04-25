#!/usr/bin/env python3
"""
Basic Babel setup
"""
from flask_babel import Babel
from flask import Flask, render_template

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Defining various class variables for babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@app.route("/", strict_slashes=False)
def home() -> str:
    """
    Displays 2  -index.html
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)