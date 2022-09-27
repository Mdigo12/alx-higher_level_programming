#!/usr/bin/python3

"""Defines a write function"""


def append_write(filename="", text=""):
    """
    Appends text to a file

    Args:
        filename (str): file to append a text
        text (str): text to be appended to the file
    Return:
        Number of characters appended
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
