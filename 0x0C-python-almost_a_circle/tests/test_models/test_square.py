#!/usr/bin/python3
"""Square.py unittest"""

import unittest
from models.square import Square
from models.base import Base

class TestSquare(unittest.TestCase):
    """Testing the class squareinstances"""

    def test_args(self):
        """ Tests on various args
        size
        2 args
        3 args
        4 args
        1st arg a string
        2nd is not an int
        3rd arg not an int
        size = 0
        x is -ve
        y is -ve
        respectively
        """
        self.assertIsInstance(Square(4), Base)
        sq = Square(3, 2)
        self.assertEqual(sq.size, 3)
        sq = Square(1, 2, 3)
        self.assertEqual(sq.x, 2)
        sq = Square(1, 2, 4, 7)
        self.assertEqual(sq.id, 7)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, "3")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 7, "3")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(2, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(2, 9, -1)

    def test_update(self):
        """Testing for update function
        no values
        one arg
        two args
        three args
        four args
        5 args
        Respectively
        """
        sq = Square(10, 10, 10, 1)
        sq.update()
        self.assertEqual("[Square] (1) 10/10 - 10", str(sq))

        sq.update(4)
        self.assertEqual("[Square] (4) 10/10 - 10", str(sq))

        sq.update(3, 4)
        self.assertEqual("[Square] (3) 10/10 - 4", str(sq))

        sq.update(3, 4, 8)
        self.assertEqual("[Square] (3) 8/10 - 4", str(sq))

        sq.update(7, 2, 3, 4)
        self.assertEqual("[Square] (7) 3/4 - 2", str(sq))


    def test_update_kwargs(self):
        """Testing update() with key/value argument
        one arg
        2 args
        3 args
        4 args
        5 args
        """
        sq = Square(10, 10, 10, 1)
        sq.update(id=4)
        self.assertEqual("[Square] (4) 10/10 - 10", str(sq))

        sq.update(id=3, size=4)
        self.assertEqual("[Square] (3) 10/10 - 4", str(sq))

        sq.update(size=2, x=4,id=1)
        self.assertEqual("[Square] (1) 4/10 - 2", str(sq))

        sq.update(id=7, size=9, x=1,y =3)
        self.assertEqual("[Square] (7) 1/3 - 9", str(sq))
