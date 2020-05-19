#!/usr/bin/python3

"""Square class with size and area"""


class Square:
    """The square object"""
    def __init__(self, size=0):
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """Finds the area of the square"""
        return self.__size * self.__size
