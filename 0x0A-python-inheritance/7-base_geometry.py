#!/usr/bin/python3
"""
A class that defines     BaseGeometry
"""


class BaseGeometry:
    """
    Class BaseGeometry
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        a method that defines object summary
        Args:
            name (str): the name paametre
            value (int): the parameter to validate
        """
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
