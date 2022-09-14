#!/usr/bin/python3

'''
a class Square that defines a square
'''


class Square:
    """
    class with private attribute size and validates it

    raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """

    def __init__(self, size=0):
        """
        Initialization
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif type < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        finding the area of the square

        Returns:
            int: the are of the square
        """
        return self.__size**2
