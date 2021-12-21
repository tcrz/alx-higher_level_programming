#!/usr/bin/python3
"""
4-from_json_string module
"""


import json


def from_json_string(my_obj):
    """
    returns an object (Python data structure) represented by a JSON string
    [Deserialization]
    """
    return json.loads(my_obj)
