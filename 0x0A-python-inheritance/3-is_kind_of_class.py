#!/usr/bin/python3

"""Defines a class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Return:
        True : If obj is an instance of or inherited instance of a class
        False : If otherwise
    """

    if isinstance(obj, a_class):
        return True
    return False
