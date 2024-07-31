#!/usr/bin/env python3
"""
Flask app with user locale selection.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _


class Config:
    """Configuration class for the Flask app."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """Returns a user dictionary or None if the ID cannot be found."""
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """Find a user if any, and set it as a global on flask.g.user."""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Select the best language for the user."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render the home page."""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
