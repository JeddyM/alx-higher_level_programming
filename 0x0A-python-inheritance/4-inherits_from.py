#!/usr/bin/python3
"""Defines the module 4-inherits_from.py"""


def inherits_from(obj, a_class):
    """Check if object is an instance of a class that inherited
    (directly or indirectly) from a class
    Args:
        obj: object
        a_class: class
    Return:
        True if obj is an inherited instance of a_class else False
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    return False
