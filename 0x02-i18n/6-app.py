#!/usr/bin/env python3
"""
Basic Babel setup
"""
from flask_babel import Babel
from flask import Flask, render_template, request, g

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    if request.args.get('locale') and request.args.get(
            'locale') in app.config['LANGUAGES']:
        return request.args.get('locale')

    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    language = request.accept_languages.best_match(app.config['LANGUAGES'])
    if language and language in app.config['LANGUAGES']:
        return language

    return app.config['BABEL_DEFAULT_LOCALE']


def get_user() -> dict:
    """get_user function to mock a database
        lookup
    """
    userId = request.args.get('login_as', None)
    if userId:
        return users.get(int(userId))
    return None


@app.before_request
def before_request():
    """find a user if any, and set it as a
        global on flask.g.user
    """
    g.user = get_user()


@app.route("/", strict_slashes=False)
def home() -> str:
    """
    Displays 6-index.html
    Translates to user's language
    Then passes it to the web
    """
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run()
