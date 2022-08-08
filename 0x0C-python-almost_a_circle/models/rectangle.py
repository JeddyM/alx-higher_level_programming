#!/usr/bin/python3
"""class rectangle module"""

from base import Base

class Rectangle(Base):
    """Defining class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method

        Args:
            width: width of rectangle
            height: height of rectangle
            x: x-axis of rectangle
            y: y-axis of rectangle
            id: rectangle id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):

    @width.setter

    def area(self):
        """Area of a rectangle
        Return: Area of rectangle
        """
        return self.width * self.height


