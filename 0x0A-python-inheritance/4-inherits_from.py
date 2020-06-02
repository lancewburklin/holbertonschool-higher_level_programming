#!/usr/bin/python3
"""
FInds if object is subclass of class
"""


def inherits_from(obj, a_class):
    """Returns false if object is of class"""
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
