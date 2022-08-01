#! /bin/python
# Name: app.py
# User: Prottush Purno
"""
Docstring:
"""
from flask import Flask

from routes import initialise_routes

app = Flask(__name__)

initialise_routes(app)
# app.add_url_rule('/', 'index', index)

if __name__ == "__main__":
    app.run(debug=True)
