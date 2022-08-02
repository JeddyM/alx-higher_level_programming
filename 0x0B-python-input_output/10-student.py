#!/usr/bin/python3
"""10-student.py Module"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializing method
        Args:
            first_name(str): first_name
            last_name(str): last_name
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """replaces all attributes of the Student instance
        Args:
            attrs: attributes
            """
        if not attrs:
            return self.__dict__
        return ({key: value for key, value in self.__dict__.items()
                if key in attrs})
