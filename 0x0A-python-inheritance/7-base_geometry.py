#!/usr/bin/python3

"""
Adds area to Geometry
"""


class BaseGeometry:
    """Geometry class"""

    def area(self):
        """Finds the area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Makes sure that it's an integer"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
