#!/usr/bin/python3

"""Square class that prints a square"""


class Square:
    """The square object"""
    __size = 0

    def __init__(self, size=0):
        """Sets the size of the square"""
        self.__size = size

    @property
    def size(self):
        """Finds the size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of a square"""
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """FInds the area of a square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints a square"""
        numMax = self.__size
        i = 0
        n = 0
        while i < numMax:
            n = 0
            while n < numMax:
                print("#", end="")
                if n == numMax - 1:
                    print("")
                n += 1
            i += 1
