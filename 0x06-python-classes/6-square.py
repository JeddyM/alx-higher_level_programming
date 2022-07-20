#!/usr/bin/python3:wq

"""Square module"""


class Square:
    """class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square class

        Args:
            size(int):  size is a private instance attribute
            position(int): poosition of the new square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get current postion of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(number, int) for number in value) or
                not all(number >= 0 for number in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square  area"""
        return (self.__size ** 2)

    def my_print(self):
        """Print in stdout a square with #"""
        if self.__size == 0:
            print("")
            return

        [print("")for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
