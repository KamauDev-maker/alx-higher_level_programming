#!/usr/bin/python3
"""
a method that defines a text file-reading function
"""


def read_file(filename=""):
    """
    Prints the content of a file to stdout
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
