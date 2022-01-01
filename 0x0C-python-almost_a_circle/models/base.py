#!/usr/bin/python3
"""
Base Class
"""
import json
import sys
import os
import csv


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
        if (type(list_dictionaries) is list and
                all(isinstance(i, dict) for i in list_dictionaries)):
            return json.dumps(list_dictionaries)
        else:
            raise TypeError("Not a list of dictionaries")

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string representation to a file"""
        if not list_objs:
            json_str = '[]'
        else:
            json_str = cls.to_json_string([i.to_dictionary()
                                           for i in list_objs])
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string:
            return '[]'
        if type(json_string) is not str:
            raise TypeError("Not a string")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy = cls(4, 3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + '.json'
        list_objs = []
        if os.path.exists(filename):
            with open(filename, encoding='utf-8') as file:
                instances = cls.from_json_string(file.read())
                for i in instances:
                    list_objs.append(cls.create(**i))
        return list_objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in csv to file"""
        if list_objs:
            if cls.__name__ == 'Rectangle':
                with open("Rectangle.csv", 'w', encoding='utf-8') as file:
                    write = csv.writer(file, delimiter=',')
                    for obj in list_objs:
                        write.writerow([obj.width, obj.height,
                                        obj.x, obj.y, obj.id])
            if cls.__name__ == 'Square':
                with open("Square.csv", 'w', encoding='utf-8') as file:
                    write = csv.writer(file, delimiter=',')
                    for obj in list_objs:
                        write.writerow([obj.size, obj.x, obj.y, obj.id])

    @classmethod
    def load_from_file_csv(cls):
        """deserialize csv to instance"""
        filename = cls.__name__ + '.csv'
        list_objs = []
        if os.path.exists(filename):
            if cls.__name__ == 'Rectangle':
                with open(filename, encoding='utf-8') as file:
                    lines = csv.reader(file)
                    for row in lines:
                        k = [int(x) for x in row]
                        dummy = cls(3, 3)
                        dummy.update(width=k[0], height=k[1],
                                     x=k[2], y=k[3], id=k[4])
                        list_objs.append(dummy)
            if cls.__name__ == 'Square':
                with open(filename, encoding='utf-8') as file:
                    lines = csv.reader(file)
                    for row in lines:
                        k = [int(x) for x in row]
                        dummy = cls(3, 3)
                        dummy.update(size=k[0], x=k[1], y=k[2], id=k[3])
                        list_objs.append(dummy)
        return list_objs
