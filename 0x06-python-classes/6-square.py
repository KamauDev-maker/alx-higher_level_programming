#!/usr/bin/python3
"""
no module imported
"""


class Square:
    """
    class that generates new square instances
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        method that helps us define properties for our object summary
        Args:
            size (int): size of the new square
            position (int): position of new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        method that retrieves the new instance
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        method that sets the new instance
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self._size = value

    @property
    def position(self):
        """
        method that retrieves the new position instance
        """
        return self._position

    @position.setter
    def position(self, value):
        """
        method that retrieves the new position instance
        """
        if not isinstance(value, tuple) or len(value) != 2
        or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """
        method that gets the area of a square
        """
        return self.size ** 2

    def my_print(self):
        """
        methods that prints the square of character #
        and the position
        """
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print(' ' * self.position[0] + '#' * self.size)
