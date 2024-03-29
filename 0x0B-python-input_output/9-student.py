#!/usr/bin/python3
"""Module 9-student.py"""


class Student:
    """Class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return vars(self)
