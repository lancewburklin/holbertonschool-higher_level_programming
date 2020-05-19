#!/usr/bin/python3

"""Square with private size"""


class Square:
    """This is an object. A square object."""

    __size = 0

    def __init__(self, size):
        """This is the size of the square"""
        Square.__size = size
