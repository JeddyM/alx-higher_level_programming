#!/usr/bin/python3
"""The module 4-from_json_string.py"""


import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string
    Args:
        my_str: string to convert to JSON
    Returns:
        object
    """
    return json.loads(my_str)
