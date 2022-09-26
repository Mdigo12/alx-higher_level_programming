#!/usr/bin/python3

"""Defines a class"""


class BaseGeometry:
    """
    creates an area method
    """

    def area(self):
        """Calculates the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the `value`
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__width, self.__height)

    def area(self):
        """"Calculates area of rectangle"""
        return self.__width * self.__height

    def __init__(self, width, height):
        """
        Initialization

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

class Square(Rectangle):
    """Represents a square as asubclass of Rectangle"""

    def __init__(self, size):
        """
        Initialization

        Args:
            size (int): Sides of a square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

