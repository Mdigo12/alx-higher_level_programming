#!/usr/bin/python3
"""class Square that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """"Represents class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of instance attributes
        Args:
            size (int): Sides of the square
            x, y, id: Inherited from class Rectangle
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """"getter method"""
        return self.width

    @size.setter
    def size(self, value):
        """setter method"""
        self.width = value
        self.height = value

    def __str__(self):
        """Overloading the special str method"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """update method for class Square"""

        if args is not None and len(args) != 0:
            list_attr = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if list_attr[i] == "size":
                    setattr(self, "width", args[i])
                    setattr(self, "height", args[i])
                else:
                    setattr(self, list_attr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == "size":
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """"Returns a dictionary representation of Square
        with keys as id, size, x, y
        """
        keys = ["id", "size", "x", "y"]
        dict_res = {}

        for key in keys:
            if key == "size":
                dict_res[key] = getattr(self, "width")
            else:
                dict_res[key] = getattr(self, key)
        return dict_res
