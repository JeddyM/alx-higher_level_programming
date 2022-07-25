#!/usr/bin/python3
'''Class Rectangle'''


class Rectangle:
    '''Define class Rectangle
    Attributes:
     number_of_instances(int): Number of instances
     print_symbol(any): symbol for string representation
    '''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Initialization of a new class rectangle instance
        Args:
        width(int): width of rectangle
        height(int): height of rectangle
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if isinstance(value, int) is False:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

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
        Rectangle.number_of_instances -= 1
