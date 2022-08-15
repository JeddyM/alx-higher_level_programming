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
        width = 0
        height = 0
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
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)


    def test_area(self):
        """Test area"""
        Rect = Rectangle(5, 3)
        self.assertEqual(15, Rect.area())

    def test_str(self):
        """Test for __str__()"""
        Rect = Rectangle(4, 10, 1, 6, 1)
        s = "[Rectangle] (1) 1/6 - 4/10"
        self.assertEqual(s, str(Rect))

    """def test_display(self):
        Testing rectangle display
        rect = Rectangle(1, 2 , 0, 1)
        output = TestRectangle_stdout.capture_stdout(rect, "display")
        self.assertEqual("\n#\n #\n", output.getvalue())"""

    def test_update(self):
        """Testing for upadte function
        no values
        one arg
        two args
        three args
        four args
        5 args
        Respectively
        """
        rect = Rectangle(10, 10, 10, 10, 1)
        rect.update()
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(rect))

        rect.update(4)
        self.assertEqual("[Rectangle] (4) 10/10 - 10/10", str(rect))

        rect.update(3, 4)
        self.assertEqual("[Rectangle] (3) 10/10 - 4/10", str(rect))

        rect.update(3, 4, 8)
        self.assertEqual("[Rectangle] (3) 10/10 - 4/8", str(rect))

        rect.update(1, 2, 3, 4)
        self.assertEqual("[Rectangle] (1) 4/10 - 2/3", str(rect))

        rect.update(7, 2, 3, 4, 6)
        self.assertEqual("[Rectangle] (7) 4/6 - 2/3", str(rect))

    def test_update_kwargs(self):
        """Testing update() with key/value argument
        one arg
        2 args
        3 args
        4 args
        5 args
        """
        rect = Rectangle(10, 10, 10, 10, 1)
        rect.update(id=4)
        self.assertEqual("[Rectangle] (4) 10/10 - 10/10", str(rect))

        rect.update(id =3, width=4)
        self.assertEqual("[Rectangle] (3) 10/10 - 4/10", str(rect))

        rect.update(id=3, width=4, height=8)
        self.assertEqual("[Rectangle] (3) 10/10 - 4/8", str(rect))

        rect.update(width=2, x=4, height=3,id=1)
        self.assertEqual("[Rectangle] (1) 4/10 - 2/3", str(rect))

        rect.update(id=7, width=9, height=11, x=1,y =3)
        self.assertEqual("[Rectangle] (7) 1/3 - 9/11", str(rect))



if __name__ == '__main__':
    unittest.main()
