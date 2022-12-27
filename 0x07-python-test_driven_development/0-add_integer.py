#!/usr/bin/python3
"""
No modules imported
"""


def add_integer(a, b=98):
    """
    Returns an integer addition of a and b

    Float are to be casted to integers

    Raises:
        TypeError: if a and b are not integers or floats
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
