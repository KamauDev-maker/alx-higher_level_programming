#!/usr/bin/python3
"""
a method that defines a file-appending function
"""


def append_write(filename="", text=""):
    """
    A method that appends a string to the end of a UTF8

    Args:
        filename (str): The name of the file to append
        text (str): the string to append to the file

    Returns:
        The number of characters to append
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
