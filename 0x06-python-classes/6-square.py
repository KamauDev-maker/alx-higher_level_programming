#!/usr/bin/python3
"""
No module imported
"""


class Square:
    """
    Private instance attribute size
    public instance method
    """

    def __init__(self, size=0, position=(0, 0)):
        """private instance attribute
        parameters
        -------------------------
        size : integer else TypeError
        if size less than 0, raise value error
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        to retrieve private instance attribute size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        to set private instance attribute
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """to retrieve private instance attribute position"""
        return self.__position

    @position.setter
    def position(self, value):
        """to set position, a tuple of two integers"""
        if not isinstance(value, tuple) or len(value) != 2 or\
                not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        public instance method
        returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        print squre using #
        """
        if self.size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
