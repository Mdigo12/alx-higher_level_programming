#!/usr/bin/python3

"""defines a student"""


class Student:
    """Represent Student"""

    def __init__(self, first_name, last_name, age):
        """
        Initialize student

        Args:
            first_name (str): Student first name
            last_name (str): Student last name
            age (int): Student name
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary representation of Student object

        If attrs is a list of strings,
        represents only those attributes included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs
                    if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
