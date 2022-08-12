#!/usr/bin/python3
"""Unittest for Base class"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test base class"""

    def test_ids(self):
        """Testing for different ids
        id doesnt exist
        id doesn't exist but previous exist
        id exists
        id doesnt exit but previous exit
        respectively
        """
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        b = Base(20)
        self.assertEqual(b.id, 20)
        b = Base()
        self.assertEqual(b.id, 3)

    def test_to_json_string(self):
        """Testing for json to string
        empty object
        object none
        """
        base_json = Base.to_json_string([])
        self.assertIsInstance(base_json, str)
        base_json = Base.to_json_string(None)
        self.assertIsInstance(base_json, str)
        base_json = Base.to_json_string([ { 'id': 12 }])
        self.assertIsInstance(base_json, str)

    def test_from_json_string(self):
        """Testing form json to string
        empty string
        string none
        id with value exists
        respectively
        """
        base_obj = Base.from_json_string("[]")
        self.assertEqual([], base_obj)
        base_obj = Base.from_json_string(None)
        self.assertEqual([], base_obj)
        base_obj = Base.from_json_string('[{ "id": 89 }]')
        self.assertIsInstance(base_obj, list)
