#!/usr/bin/python3
"""
Be here or be Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """HERE IT IS ALL SQUARE"""

    def __init__(self, size, x=0, y=0, id=None):
        """Init function"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Square info"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height)
