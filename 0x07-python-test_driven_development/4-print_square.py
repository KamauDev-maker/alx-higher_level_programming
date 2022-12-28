#!/usr/bin/python3
"""
No module imported
"""


def print_square(size):
    """
    methods that defines the object property summary

    size:is the size lenght of the square
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
