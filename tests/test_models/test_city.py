#!/usr/bin/python3
"""test module for City class"""
import unittest
from models.city import City
from models.base_model import BaseModel
from unittest.mock import patch
from io import StringIO
import sys
from datetime import timedelta
from datetime import datetime

class TestUser(unittest.TestCase):
    """ basic type-checking tests of attibutes in  the `City` class"""

    def test_types(self):
        """confirm types of the custom argumenta"""
        c0a = City()
        self.assertTrue(type(c0a.name), str)
        self.assertTrue(type(c0a.state_id), str)


    def test_subclass(self):
           """checks inheritance of `City` objects"""
           c0 = City()
           self.assertIsInstance(c0,City)
           self.assertTrue(issubclass(type(c0),BaseModel))

class TestUserInstantiation(unittest.TestCase):
    """checks that the instantiation of `City` objects
    works correctly in various scenarios"""

    def test_init_no_args(self):
        """instantiation test with no arguments"""
        c1 = City()
        self.assertEqual(isinstance(c1, City), True)
        self.assertTrue(hasattr(c1, "created_at"))
        self.assertTrue(hasattr(c1, "updated_at"))
        self.assertTrue(hasattr(c1, "id"))
        self.assertAlmostEqual(c1.created_at, c1.updated_at,
                               delta=timedelta(seconds=1))
        self.assertTrue(hasattr(c1, "name"))
        self.assertTrue(hasattr(c1, "state_id"))


    def test_init_custom_args(self):
        """instantiation test of it's own  arguments"""
        c1a = City()
        self.assertEqual(isinstance(c1a, City), True)
        self.assertEqual(c1a.name, "")
        self.assertTrue(type(c1a.state_id), str)

        c1a.first_name = "Minna"
        self.assertEqual(c1a.first_name, "Minna")

    def test_init_with_args(self):
        """tests instantiation of object with arguments from dictionary"""
        dict1 = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                 'created_at': '2017-09-28T21:03:54.052298',
                 '__class__': 'City',
                 'updated_at': '2017-09-28T21:03:54.052302',
                 'name': 'Abuja'}
        c2 = City(**dict1)
        self.assertTrue(hasattr(c2, "created_at"))
        self.assertIsInstance(c2.created_at, datetime)
        self.assertIsInstance(c2.updated_at, datetime)
        self.assertEqual(c2.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")


    def test_init_with_kwargs(self):
        """tests instantiation of object with direct kwargs"""
        c3 = City(id="78393",
                       created_at="2023-12-14T17:30:54.052298",
                       updated_at="2024-01-02T11:03:54.062721")
        self.assertEqual(type(c3.id), str)
        self.assertEqual(type(c3.created_at), datetime)


class TestUserMethods(unittest.TestCase):
    """ tests the methods of the `City` classs"""

    @patch('builtins.print')
    def test_str_method(self, mock_output):
        """checks that the output of `str()` matches the requirements"""
        c4 = City()
        c4.name = "first model"
        c4.number = "30"
        mod_str = f"[{c4.__class__.__name__}] ({c4.id}) {c4.__dict__}"
        output_of_str = str(c4)
        print(c4)
        self.assertEqual(output_of_str, mod_str)
        mock_output.assert_called_once_with(c4)

    def test_to_dict(self):
        """ checks that the output of `to_dict()` matches requirements"""
        c5 = City()
        c5.name = "new model"
        c5.number = 54
        mod_dict_str = c5.to_dict()
        self.assertEqual(type(mod_dict_str), dict)
        self.assertIn("City", c5.to_dict().values())
        self.assertIn("id", c5.to_dict().keys())
        self.assertEqual(type(mod_dict_str['created_at']), str)
        self.assertEqual(type(mod_dict_str['updated_at']), str)

    # def test_save(self):
    #     """checks that the updated_at attribute is updated with save() """
    #     c6 = City()
    #     # print(f"created at: {c6.created_at}")
    #     # print(f"update 0: {c6.updated_at}")
    #     self.assertAlmostEqual(c6.created_at, c6.updated_at,
    #                            delta=timedelta(seconds=1))
    #     c6.save()
    #     # print(f"update 1: {c6.updated_at}")
    #     self.assertNotAlmostEqual(c6.created_at, c6.updated_at,
    #                               delta=timedelta(microseconds=10))
    #     c6.save()
    #     # print(f"update 2: {c6.updated_at}")
    #     self.assertNotAlmostEqual(c6.created_at, c6.updated_at,
    #                               delta=timedelta(microseconds=1000))
