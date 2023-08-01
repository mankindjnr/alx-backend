#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
"""
i18n tasks with flask and python
"""


app = Flask(__name__)


@app.route('/')
def index():
    """Display Hello HBNB!"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
