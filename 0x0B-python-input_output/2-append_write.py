#!/usr/bin/python3
"""2-append_write.py module"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    Args:
        filename: file name
        text(str): text to append
    Returns:
        number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        if f.write(text):
            return len(text)
