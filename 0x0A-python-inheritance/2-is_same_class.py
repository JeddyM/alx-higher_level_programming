#!/usr/bin/python3
"""Defines module 2-is_same_class.py"""


def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of the specified class
    Args:
        obj: object
        a_class: class to check
    Returns:
        True if its an instance else False
    """
    if type(obj) is a_class:
        return True
    return False
