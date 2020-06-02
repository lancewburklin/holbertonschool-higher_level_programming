#!/usr/bin/python3

"""
Creates a square based off the rectangle
"""


rect = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(rect):
    """The square class"""

    def __init__(self, size):
        """Initializes the square"""
        super().__init__(size, size)
        bg = BaseGeometry()
        bg.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Finds the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Prints info for square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
