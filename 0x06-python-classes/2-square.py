#!/usr/bin/python3
"""Square module"""


class Square:
    """class Square"""
    def __init__(self, size=0):
        """Initialize the square class

        Args:
        size(int):  size is a private instance attribute
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
