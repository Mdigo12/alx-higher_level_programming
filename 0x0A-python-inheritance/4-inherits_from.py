#!/usr/bin/python3

"""Defines a class-checking function."""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class
    that inherited (directly or indirectly) from the specified class

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Return:
        True : If obj is an instance of a class
            that inherited (directly or indirectly) from the specified class
        False : If otherwise
    """

    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
