#!/usr/bin/python3
"""Defines module 3-is_kind_of_class.py"""


def is_kind_of_class(obj, a_class):
    """Determines if object is of instance of a classs or of
    class inherited from it
    Args:
        obj: object
        a_class: class
    Returns:
        True if object is instance of class/class base else False
    """
    if isinstance(obj, a_class):
        return True
    return False
