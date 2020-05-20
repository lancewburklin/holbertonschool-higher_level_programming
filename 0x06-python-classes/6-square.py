#!/usr/bin/python3

"""Square class that prints a square"""


class Square:
    """The square object"""
    __size = 0
    __position = 0

    def __init__(self, size=0, position=(0, 0)):
        """Sets the size of the square"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Sets the posiotion of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square"""
        elerror = 'position must be a tuple of 2 positive integers'
        if type(value) is tuple and len(value) == 2:
            if (isinstance(value[0], int), isinstance(value[1], int)):
                if (value[0] >= 0 and value[1] >= 0):
                    self.__position = value
                else:
                    raise TypeError(elerror)
            else:
                raise TypeError(elerror)
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """FInds the area of a square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints a square"""
        numMax = self.__size
        i = 0
        n = 0
        x = 0
        if numMax == 0:
            print("")
            return
        while x < self.__position[1]:
            print()
            x += 1
        while i < numMax:
            n = 0
            print(" " * self.__position[0], end="")
            while n < numMax:
                print("#", end="")
                if n == numMax - 1:
                    print("")
                n += 1
            i += 1
