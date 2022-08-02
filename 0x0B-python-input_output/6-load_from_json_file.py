#!/usr/bin/python3
"""6-load_from_json_file.py module"""


def load_from_json_file(filename):
    """creates an Object from a “JSON file”
    Args:
        filename: file name
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
