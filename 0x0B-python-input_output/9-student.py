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

    def to_json(self):
        """Json representation of Student object"""
        return self.__dict__
