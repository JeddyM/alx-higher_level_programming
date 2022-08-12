#!/usr/bin/python3
"""Unittest for the rectangle module"""


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test class Rectangle"""

    def test_args(self):
        """ Tests on various args
        width and height
        3 args
        4 args
        5 args
        1st arg a string
        3rd is not an int
        4th args not an int
        respectively
        """
        self.assertIsInstance(Rectangle(9, 4), Base)
        Rect = Rectangle(1, 2, 3)
        self.assertEqual(Rect.width, 1)
        Rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(Rect.height, 2)
        Rect = Rectangle(1, 2, 3, 4, 7)
        self.assertEqual(Rect.id, 7)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, "1")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("8", 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 1, "3")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 1, 6, "10")


if __name__ == '__main__':
    unittest.main()
