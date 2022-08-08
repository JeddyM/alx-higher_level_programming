#!/usr/bin/python3
"""Module for square.py"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Defining class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """" Initialized method
        Args:
            size: square size
            x: x axis/ coordinate
            y: y-axis/ coordinate
            id: object id
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>"""

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
