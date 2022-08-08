#!/usr/bin/python3
"""class rectangle module"""


from models.base import Base


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
        """width getter with private attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """"width setter function
        Args:
            value: value
        """
        if type(value) is not int:
            raise TypeError("width must be be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter with private attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """"height setter function
        Args:
            value: value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """X getter function"""
        return self.__x

    @x.setter
    def x(self, value):
        """X setter function"""
        if type(value) is not int:
            raise TypeError("x must be be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter function"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter function"""
        if type(value) is not int:
            raise TypeError("y must be be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of a rectangle
        Return: Area of rectangle
        """
        return self.width * self.height

    def display(self):
        """Prints the rectangle with character #"""
        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for j in range(self.width)]
            print("")

    def __str__(self):
        """Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
    def update(self, *args):
        """"Assigns an argument to each attribute
        Args:
            arguments
        """
