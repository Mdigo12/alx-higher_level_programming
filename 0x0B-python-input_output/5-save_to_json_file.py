#!/usr/bin/python3

"""writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """writes a file with a json representation of an object"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
