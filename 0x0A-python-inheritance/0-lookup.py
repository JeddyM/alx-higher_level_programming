#!/usr/bin/python3
"""Module for listing attributes"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object

    args:
        obj: object
    Return:
        a list of object
    """
    return dir(obj)
