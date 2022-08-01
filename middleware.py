#! /bin/python
# Name: .py 
# User: Prottush Purno
"""
Docstring: 
"""
from os import abort

from flask import jsonify, request

heroes = [{'name': 'John Smith', 'nationality': 'British', 'occupation': 'Doctor'},
          {'name': 'Elon Musk', 'nationality': 'South African', 'occupation': 'Entrepreneur'},
          {'name': 'Bob', 'nationality': 'USA', 'occupation': 'Pilot'}
          ]


def index():
    return "Hello World"


def db():
    return "Hello DB grads"


def user_profile(id):
    return f"Profile page of user #{id}"


def hero():
    return jsonify(heroes)


def hero_add():
    try:
        data = request.get_json(force=True)
        name = data['name']
        nationality = data['nationality']
        occupation = data['occupation']
        if name and nationality and occupation:
            heroes.append({'name': name, 'nationality': nationality,
                           'occupation': occupation})
            return jsonify({"Hero "+ name: " Added successfully"})
    except Exception as err:
        print(err)
        abort(400)
    return None

