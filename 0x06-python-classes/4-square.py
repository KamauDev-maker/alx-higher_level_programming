#!/usr/bin/python3
"""
no module imported
"""


class Square:
    """
    class that generate new instances of square
    """
    def __init__(self, size=0):
        """
        method that helps us define properties for object summary

        Args:
            size (int): The size of the new square
        """
        self.size = size

    @property
    def size(self):
        """
        method that helps retrieve new instance
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        method that helps set the new instance
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        methods returns the area of the square
        """
        return self.__size ** 2
