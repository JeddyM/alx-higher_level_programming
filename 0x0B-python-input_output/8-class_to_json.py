#!/usr/bin/python3
"""Module 8-class_to_json.py"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    for JSON serialization of an object
     Args:
        obj
    """
    # The vars() function returns the __dic__ attribute of an object.
    return vars(obj)
