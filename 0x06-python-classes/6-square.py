#!/usr/bin/python3
"""
no module imported
"""


class Square:
    """
    class that generate new instances of square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        method that helps us define properties for object summary

        Args:
            size (int): The size of the new square
            position (int): position of the new square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        method that helps retrieve new instance position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        method that helps set the new instance position
        """
        if not isinstance(value, tuple) or 
        len(value) != 2 or not all(isinstance(i, int) and 
                i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integes")
        self.__position = value

    def area(self):
        """
        methods returns the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints the square with chacter #
        """
        if self.size == 0:
            print()
            return
        for i in range(self.position[i]):
            print()
        for i in range(self.size):
            print('' * self.position[0] + '#' * self.size)
