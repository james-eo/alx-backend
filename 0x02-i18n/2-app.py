#!/usr/bin/env python3
"""
Basic Flask app with locale selection.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Defines the class config for the configuration of flask app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determine the best match with the supported languages.

    Returns:
        str: The best match locale.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the index page with a welcome message.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
