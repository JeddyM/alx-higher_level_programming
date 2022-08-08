#!/usr/bin/python3
"""The base class module"""


class Base:
    """The base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialized method
        Args:
            id (int): id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
