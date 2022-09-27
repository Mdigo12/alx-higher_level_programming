#!/usr/bin/python3

"""Defines an object as represented in JSON"""
import json


def from_json_string(my_str):
    """Converts a json string back to an object

    Args:
        my_str (str): a json string to be deserialized

    Returns:
        An object (Python data structure)
    """
    return json.loads(my_str)
