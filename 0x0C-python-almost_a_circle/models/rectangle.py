#!/usr/bin/python3
"""
Rectangle module
"""


from models.base import Base


class Rectangle(Base):
    """The rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width"""
        Rectangle.int_validator(value, "width")
        self.__width = value

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""
        Rectangle.int_validator(value, "height")
        self.__height = value

    @property
    def x(self):
        """Gets x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x"""
        Rectangle.int_validator(value, "x")
        self.__x = value

    @property
    def y(self):
        """gets y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y"""
        Rectangle.int_validator(value, "y")
        self.__y = value

    def int_validator(value, attr):
        """Validates attributes"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attr))
        if value < 0 and attr in {"x", "y"}:
            raise ValueError("{} must be >= 0".format(attr))
        if value <= 0 and attr in {"height", "width"}:
            raise ValueError("{} must be > 0".format(attr))

    def area(self):
        """Finds the area"""
        return self.__height * self.__width
