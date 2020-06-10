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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Gets a dictionary and converts it to string"""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON info to a file"""
        the_list = []
        if list_objs is not None:
            for stuff in list_objs:
                new_stuff = stuff.to_dictionary()
                the_list.append(new_stuff)
        the_list = Base.to_json_string(the_list)
        with open("{}.json".format(cls.__name__), mode='w') as f:
            f.write(str(the_list))

    @staticmethod
    def from_json_string(json_string):
        """Changes it over"""
        if json_string is None:
            return []
        return json.loads(json_string)
