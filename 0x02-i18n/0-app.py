#!/usr/bin/env python3
"""
Basic Flask app to display a welcome message.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Render the index page with a welcome message.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
