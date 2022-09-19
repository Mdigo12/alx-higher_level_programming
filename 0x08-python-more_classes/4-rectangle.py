#!/usr/bin/python3

"""1-rectangle module"""


class Rectangle:
    """Creates a class Rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initialization with two instance attibutes
        arg: width
        arg: height
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """
        Validate the value passed
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """
        Validate the value passed
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Calculates area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """
        Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """

        rec = ""
        if (self.__width == 0 or self.__height == 0):
            return("")
        for i in range(self.__height):
            rec += "#"*self.__width
            if i + 1 < self.__height:
                rec += '\n'
        return rec

    def __repr__(self):
        """
        return: representation of rectangle that can be used by eval()
        to create new object
        """

        rec = "Rectangle(" + str(self.__width) + "," + str(self.__height) + ")"
        return rec
