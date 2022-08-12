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

    def update(self, *args, **kwargs):
        """"Assigns an argument to each attribute
        Args:
            non
        """
        if args:
            i = 0
            listargs = ['id', 'size', 'x', 'y']
            for arg in args:
                setattr(self, listargs[i], arg)
                i += 1
            return
        else:
            for key, value in kwargs.items():
                '''setatr maps key to value for **kwargs'''
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a square
        Return:
            dictionary: with id, size x & y
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
