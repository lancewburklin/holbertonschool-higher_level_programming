#!/usr/bin/python3

"""A square class with some info"""


class Square:
    """The square object"""
    __size = 0

    def __init__(self, size=0):
        """Sets the size of the square"""
        self.__size = size

    @property
    def size(self):
        """Size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """Finds the area of the square"""
        return self.__size * self.__size
