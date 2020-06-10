#!/usr/bin/python3
"""
Creating the Base class
"""
import json


class Base:
    """Here it is"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes ID"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def to_json_string(list_dictionaries):
        """Gets a dictionary and converts it to string"""
        if not list_dictionaries or list_dictionaries is None:
            return "\"[]\""
        return json.dumps(list_dictionaries)
