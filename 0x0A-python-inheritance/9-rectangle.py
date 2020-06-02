#!/usr/bin/python3

"""
Creating a rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Init method"""
        bg = BaseGeometry()
        bg.integer_validator("width", width)
        bg.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Finds the are of the rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """Prints info for rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
