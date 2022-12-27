#!/usr/bin/python3
"""
No modules imported
"""


def add_integer(a, b=98):
"""
Returns an integer addition of a and b

Float are to casted to integers

Raises:
    TypeError: if a and b are not integers and floats
"""
if not (isinstance(a, (int, float)) and\
        isinstance(b, (int, float))):
    raise TypeError("a and b must be integers or floats")
a = int(a)
b = int(b)
return a + b
