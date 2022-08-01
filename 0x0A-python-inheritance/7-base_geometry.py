#!/usr/bin/python3
"""Defines module 7-base_geometry.py"""


class BaseGeometry:
    """Class"""
    def area(self):
        """Raises an Exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
        Args:
            name(str):a string always
            value(int): if not int raise a TypeError with message,<=
            0 raise a ValueError with message
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
