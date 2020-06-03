#!/usr/bin/python3
"""
Module creates the Student
"""


class Student:
    """Here it is"""

    def __init__(self, first_name, last_name, age):
        """Initializes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets the dictionary"""
        return self.__dict__
