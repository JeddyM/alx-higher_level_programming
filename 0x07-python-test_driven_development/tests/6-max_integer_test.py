#!/usr/bin/python3
"""Unittest for max_integer()"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for max_integer test cases"""

    def test_max_integer(self):
        """correct output cases"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 3, 5]), 5)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([10, -1, 23, -10]), 23)
        self.assertEqual(max_integer([0.4, 9.9, -6.5, 9.95]), 9.95)

    if __name__ == "__main__":
        unittest.main()
