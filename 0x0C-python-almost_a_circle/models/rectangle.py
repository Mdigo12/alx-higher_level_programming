#!/usr/bin/python3

"""Define a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Represent class Rectangle that inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialization of class Rectangle

        Args:
            width (int): parameter value (rectangle width)
            height (int): parameter value (rectangle height)
            x (int): parameter value
            y (int): paraeter value

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Defines the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """
        while self.y:
            print("")
            self.y -= 1

        for i in range(self.height):
            for j in range(self.width):
                if self.x > 0 and j == 0:
                    for n in range(self.x):
                        print(" "*self.x, end='')
                print("#", end="")
                if j == self.width - 1:
                    print("")

    def __str__(self):
        """Print string rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update rectangle class"""

        if args is not None and len(args) != 0:
            list_atr = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ the dictionary representation of a Rectangle
        with keys as id, width, height, x, y

        Returns:
            Dictionary representation of a rectangle
        """

        keys = ["id", "width", "height", "x", "y"]
        dict_res = {}

        for key in keys:
            """loop though each key
            and assign it its specific value in the dictionary
            """
            dict_res[key] = getattr(self, key)
        return dict_res
