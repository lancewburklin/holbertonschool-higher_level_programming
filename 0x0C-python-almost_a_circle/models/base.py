#!/usr/bin/python3
"""
Creating the Base class
"""


class Base:
    """Here it is"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes ID"""
        if id != None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
