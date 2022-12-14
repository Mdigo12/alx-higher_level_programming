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
