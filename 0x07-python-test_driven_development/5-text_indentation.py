#!/usr/bin/python3
"""Module for text_indentation(text) function"""


def text_indentation(text):
    """Prints a text with 2 new lines after these characters: ., ? and :
    Args:
        text(str): text to indent
    """
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    c = ""
    for i in text:
        if i in ['.', '?', ':']:
            c += i
            print("{:s}\n".format(c.strip()))
            c = ""
        else:
            c += i
    if c != "":
        print(c.strip(), end="")
