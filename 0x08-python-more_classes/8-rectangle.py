#!/usr/bin/python3

"""1-rectangle module"""


class Rectangle:
    """Creates a class Rectangle

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialization with two instance attibutes
        arg: width
        arg: height
        """
        self.height = height
        self.width = width

        Rectangle.number_of_instances += 1

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
            rec += str(self.print_symbol) * self.__width
            if i + 1 < self.__height:
                rec += '\n'
        return rec

    def __repr__(self):
        """
        return: representation of rectangle that can be used by eval()
        to create new object
        """

        rec = "Rectangle(" + str(self.__width)\
            + ", " + str(self.__height) + ")"
        return rec

    def __del__(self):
        """
        Print a message for every deletion of a Rectangle.
        And deduct one instance(deleted) from total instances
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares the areas of the two rectangles
        Returns: the rect with a bigger area or rect_1 if equal
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
