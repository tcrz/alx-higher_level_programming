#!/usr/bin/python3
"""
3-to_json_string module
"""


import json


def to_json_string(my_obj):
    """
    returns JSON representation of an object as a string
    [Serialization]
    """
    return json.dumps(my_obj)
