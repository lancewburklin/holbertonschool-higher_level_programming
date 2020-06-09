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

    def display(self):
        """Displays the rectangle"""
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Returns info for the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updates the rectangle"""
        counter = 1
        for i in args:
            if counter == 1:
                self.id = args[0]
            if counter == 2:
                self.__width = args[1]
            if counter == 3:
                self.__height = args[2]
            if counter == 4:
                self.__x = args[3]
            if counter == 5:
                self.__y = args[4]
            counter += 1
        if len(args) < 6:
            if len(args) < 1 and 'id' in kwargs.keys():
                self.id = kwargs['id']
            if len(args) < 2 and 'width' in kwargs.keys():
                self.__width = kwargs['width']
            if len(args) < 3 and 'height' in kwargs.keys():
                self.__height = kwargs['height']
            if len(args) < 4 and 'x' in kwargs.keys():
                self.__x = kwargs['x']
            if len(args) < 5 and 'y' in kwargs.keys():
                self.__y = kwargs['y']

    def to_dictionary(self):
        """Gets the square as a dictionary"""
        dictio = {'id': self.id, 'width': self.__width,
                  'height': self.__height, 'x': self.__x, 'y': self.__y}
        return dictio
