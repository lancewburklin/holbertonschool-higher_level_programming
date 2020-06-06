#!/usr/bin/python3
"""
Rectangle module
"""


from models.base import Base


class Rectangle(Base):
    """The rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @property
    def x(self):
        """Gets x"""
        return self.__x

    @property
    def y(self):
        """gets y"""
        return self.__y

    def int_validator(self, value, attr):
        """Validates attributes"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attr))
        if value <= 0:
            raise ValueError("{} must be >= 0".format(attr))

    @width.setter
    def width(self, value):
        """Sets width"""
        Rectangle.int_validator(value, width)
        self.__width = value

    @height.setter
    def height(self, value):
        """ Sets height"""
        Rectangle.int_validator(value, height)
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets x"""
        Rectangle.int_validator(value, x)
        self.__x = x

    @y.setter
    def y(self, value):
        """Sets y"""
        Rectangle.int_validator(value, y)
        self.__y = y
