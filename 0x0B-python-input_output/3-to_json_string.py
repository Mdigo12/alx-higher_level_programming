#!/usr/bin/python3

"""Defines a JSON representation of an object"""
import json


def to_json_string(my_obj):
    """Converts an object to a string

    Args:
        my_obj (object): Object to be coverted to string
    """
    return json.dumps(my_obj)
