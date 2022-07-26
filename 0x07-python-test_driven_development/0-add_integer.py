#!/usr/bin/python3
'''Module for the add_integer function'''


def add_integer(a, b=98):
    '''A function that adds 2 integers

    Args:
        a: first integer
        b: second integer

    Raises:
        TypeError: if the inputs are neither integers or float

    Return:
        sum of a and b
    '''
    if isinstance(a, (int, float)) is False:
        raise TypeError('a must be an integer')
    if isinstance(b, (int, float)) is False:
        raise TypeError('b must be an integer')
    return int(a + b)
