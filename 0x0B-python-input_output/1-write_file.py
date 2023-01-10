#!/usr/bin/python3
"""
a method that defines a file-writing function
"""


def write_file(filename="", text=""):
    """
    Write a string to a UTF8 text file.

    Args:
        filename (str): the name of the file to write
        text (str): the text to write to the file
    Returns:
        the number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
