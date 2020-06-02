#!/usr/bin/python3
"""
Finds if object is a sub class of class or is class
"""


def is_kind_of_class(obj, a_class):
    """Returns true if yes"""
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
