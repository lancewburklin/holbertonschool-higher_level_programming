#!/usr/bin/python3

"""This module adds to integers"""


def add_integer(a, b=98):
    """Here is where the math takes place"""
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return(a + b)
