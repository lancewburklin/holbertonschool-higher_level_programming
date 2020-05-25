#!/usr/bin/python3

"""
Rectangle class part two
"""


class Rectangle:
    """Here it is!"""
    __width = 0
    __height = 0
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes height and width"""
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        if type(value) == int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError('width must be >= 0')
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        """retrieves the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a rectangle"""
        if type(value) == int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError('height must be >= 0')
        else:
            raise TypeError('height must be an integer')

    def area(self):
        """gets the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Find the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Prints the rectangle"""
        recTangle = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        i = 0
        while i < self.__height:
            x = self.print_symbol
            if i != self.__height - 1:
                recTangle = recTangle + (str(x) * self.__width) + '\n'
            else:
                recTangle = recTangle + (str(x) * self.__width)
            i += 1
        return recTangle

    def __repr__(self):
        """Gets the height and width of the rectangle"""
        x = str(self.__width)
        y = str(self.__height)
        return "Rectangle(" + x + ", " + y + ")"

    def __del__(self):
        """Deletes a rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """Finds the largest area of two rectangles"""
        if type(rect_1) != Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) != Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        ar1 = rect_1.area()
        ar2 = rect_2.area()
        if ar1 >= ar2:
            return rect_1
        else:
            return rect_2
