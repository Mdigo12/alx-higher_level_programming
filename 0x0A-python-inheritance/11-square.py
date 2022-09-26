#!/usr/bin/python3
"""Defines a square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """
        Initialization

        Args:
            size (int): side of a square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
