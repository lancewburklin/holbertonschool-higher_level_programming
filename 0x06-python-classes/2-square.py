#!/usr/bin/python3

"""Square class"""


class Square:
    """This is a square and an object"""
    __size = 0

    def __init__(self, size=0):
        """Initializes the square"""
        if type(size) is int:
            if(size >= 0):
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
