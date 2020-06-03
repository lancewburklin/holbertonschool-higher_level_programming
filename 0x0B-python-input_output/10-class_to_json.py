#!/usr/bin/python3
"""
Gets dictionary of an object
"""


def class_to_json(obj):
    """Gets the dictionary of the object"""
    return obj.__dict__
