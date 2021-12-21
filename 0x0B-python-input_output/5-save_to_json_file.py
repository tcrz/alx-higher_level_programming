#!/usr/bin/python3
"""
5-save_to_json_file module
"""


import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation
    [Serialization]
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
