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

    @property
    def size(self):
        """Gets size"""
        return self.height

    @size.setter
    def size(self, value):
        """Sets the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the square"""
        counter = 1
        for i in args:
            if counter == 1:
                self.id = args[0]
            if counter == 2:
                self.size = args[1]
            if counter == 3:
                self.x = args[2]
            if counter == 4:
                self.y = args[3]
            counter += 1
        if len(args) < 5:
            if len(args) < 1 and 'id' in kwargs.keys():
                self.id = kwargs['id']
            if len(args) < 2 and 'size' in kwargs.keys():
                self.size = kwargs['size']
            if len(args) < 3 and 'x' in kwargs.keys():
                self.x = kwargs['x']
            if len(args) < 4 and 'y' in kwargs.keys():
                self.y = kwargs['y']
