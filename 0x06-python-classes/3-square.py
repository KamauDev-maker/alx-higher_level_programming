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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        methods returns the area of the square
        """
        return self.__size ** 2
