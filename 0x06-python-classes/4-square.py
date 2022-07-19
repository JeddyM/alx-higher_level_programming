#!/usr/bin/python3
"""Square module"""

class Square:
    """class Square"""
    def __init__(self, size=0):
        """Initialize the square class

        Args:
            size(int):  size is a private instance attribute
        """
        self.__size = size

    @property
    def size(self):
        """get the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area

        Returns:
            size squared
        """
        return (self.__size ** 2)
