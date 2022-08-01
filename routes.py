#! /bin/python
# Name: routes.py
# User: Prottush Purno
"""
Docstring: 
"""
from middleware import index, db


def initialise_routes(app):
    if app:
        app.add_url_rule('/api/hello/', 'index', index)
        app.add_url_rule('/api/db/', 'db', db)
        app.add_url_rule('/api/', 'list_routes', list_routes, methods=['GET'], defaults={'app': app})
    return None


def list_routes(app):
    for route in app.url_map.iter_rules():
        print(route)
    return "Routes info"
