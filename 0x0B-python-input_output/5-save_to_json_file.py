#!/usr/bin/python3
"""5-save_to_json_file.py module"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation
    Args:
        my_obj: object
        filename: filename
    """

    with open(filename, 'w', encoding="utf-8") as f:
        text = json.dumps(my_obj)
        return f.write(text)
