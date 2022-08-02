#!/usr/bin/python3
"""1-write_file.py Module"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) & returns the number
    of characters written:
        Args:
            filename: file name
            text: string to add
    """
    with open(filename, 'w', encoding="utf-8") as f:
        file_content = f.write(str(text))
        return len(text)
