#!/usr/bin/python3
"""Print name module"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>
    Args:
        first_name(str): first name
        last_name(str): last name
        """
    if isinstance(first_name, str) is False:
        raise TypeError('first_name must be a string')
    if isinstance(last_name, str) is False:
        raise TypeError('last_name must be a string')
    print(f"My name is {first_name} {last_name}")
