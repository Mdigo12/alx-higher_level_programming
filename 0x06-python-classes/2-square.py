#!/usr/bin/python3

'''
a class Square that defines a square
'''


class Square:
    """
    class with private attribute size and raises errors
    """

    def __init__(self, size=0):
        """
        Initialization
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
