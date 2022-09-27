#!/usr/bin/python3

"""Defines a write function"""


def write_file(filename="", text=""):
    """
    Writes text to a file

    Args:
        filename (str): file to write a text
        text (str): text to be written to the file

    Returns:
        Number of characters printed
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
