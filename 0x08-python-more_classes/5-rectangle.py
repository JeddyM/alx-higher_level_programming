#!/usr/bin/python3
'''Class Rectangle'''


class Rectangle:
    '''Define class Rectangle'''

    def __init__(self, width=0, height=0):
        '''Initialization of a new class rectangle instance
        Args:
        width(int): width of rectangle
        height(int): height of rectangle
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle

        Returns:
            Width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ Gets height of Rectangle

        Returns:
            height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Methodd that returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for row in range(self.__height - 1):
            print("#" * self.__width)
        return ('#' * self.__width)

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Print a message after an instance of rectangle is deleted"""
        print("Bye rectangle...")
