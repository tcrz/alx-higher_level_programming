#!/usr/bin/python3
"""
6-load_from_json_file module
"""


import json


def load_from_json_file(filename):
    """creates an Object from a JSON file"""

    with open(filename) as file:
        return json.load(file)
