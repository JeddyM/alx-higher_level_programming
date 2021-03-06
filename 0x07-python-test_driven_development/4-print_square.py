#!/usr/bin/python3
"""Module for sprint square function"""


def print_square(size):
    """prints a square with the character #"""
    if isinstance(size, int) is False:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size < 0 and isinstance(size, float) is True:
        raise TypeError('size must be an integer')
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
