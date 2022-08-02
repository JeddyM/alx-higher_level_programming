#!/usr/bin/python3
"""11-student.py Module"""


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
        """retrieves a dictionary representation of a Student
        Args:
            attrs: attributes
            """
        if not attrs:
            return self.__dict__
        return ({key: value for key, value in self.__dict__.items()
                if key in attrs})

        def reload_from_json(self, json):
            """ replaces all attributes of the Student
            Args:
                json: key/value to replace attributes
            """
            self.__dict__.update(json)
