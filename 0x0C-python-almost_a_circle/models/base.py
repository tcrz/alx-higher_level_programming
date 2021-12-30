#!/usr/bin/python3
"""
Base Class
"""
import json


class Base:
    """defining base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialises instance of a Base class"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base. __nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return '[]'
        if (type(list_dictionaries) and
                all(isinstance(i, dict) for i in list_dictionaries)):
            return json.dumps(list_dictionaries)
        else:
            raise TypeError("Not a list of dictionaries")
