#!/usr/bin/env python3
"""
Basic Babel setup
"""
from flask_babel import Babel, gettext as _
from flask import Flask, render_template, request


class Config(object):
    """
    Defining various class variables for babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determines the locale used in language translation
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def home() -> str:
    """
    Displays 3-index.html
    Translates to user's language
    Then passes it to the web
    """
    title = _('home_title')
    header = _('home_header')
    return render_template("3-index.html", title=title, header=header)


if __name__ == "__main__":
    app.run()
