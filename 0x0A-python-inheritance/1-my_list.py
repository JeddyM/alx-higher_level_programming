#!/usr/bin/python3
"""Module for a class to inherit from list"""


class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """Prints a sorted list (ascending)"""
        print(sorted(self))
