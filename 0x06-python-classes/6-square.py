#!/usr/bin/python3

'''
a class Square that defines a square
'''


class Square:
    """
    class with private attribute size
    and postion and validates it

    raises:
        TypeError: size must be an integer >= 0
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialization
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        errmsg = "position must be a tuple of 2 positive integers"

        if value is None:
            raise TypeError(errmsg)
        if type(value) != tuple:
            raise TypeError(errmsg)
        if len(value) < 2:
            raise TypeError(errmsg)
        for i in value:
            if i < 0:
                raise TypeError(errmsg)
            elif type(i) != int:
                raise TypeError(errmsg)
        self.__position = value

    def area(self):
        """
        finding the area of the square

        Returns:
            int: the are of the square
        """
        return self.__size**2

    def my_print(self):
        """
        Printing the size of the square
        """
        if self.__size == 0:
            print()
        for r in range(self.__size):
            print(" "*self.position[0], end="")
            print("#"*self.__size)
