#!/usr/bin/python3
"""test module for User class"""
import unittest
from models.user import User
from models.base_model import BaseModel
from unittest.mock import patch
from io import StringIO
import sys
from datetime import timedelta
from datetime import datetime

class TestUser(unittest.TestCase):
    """ basic type-checking tests of attibutes in  the `User` class"""

    def test_types(self):
        """confirm types of the custom argumenta"""
        u0a = User()
        self.assertTrue(type(u0a.password), str)
        self.assertTrue(type(u0a.email), str)
        self.assertTrue(type(u0a.first_name), str)
        self.assertTrue(type(u0a.last_name), str)

    def test_subclass(self):
           """checks inheritance of `User` objects"""
           u0 = User()
           self.assertIsInstance(u0,User)
           self.assertTrue(issubclass(type(u0),BaseModel))

class TestUserInstantiation(unittest.TestCase):
    """checks that the instantiation of `User` objects
    works correctly in various scenarios"""

    def test_init_no_args(self):
        """instantiation test with no arguments"""
        u1 = User()
        self.assertEqual(isinstance(u1, User), True)
        self.assertTrue(hasattr(u1, "created_at"))
        self.assertTrue(hasattr(u1, "updated_at"))
        self.assertTrue(hasattr(u1, "id"))
        self.assertAlmostEqual(u1.created_at, u1.updated_at,
                               delta=timedelta(seconds=1))
        self.assertTrue(hasattr(u1, "email"))
        self.assertTrue(hasattr(u1, "password"))
        self.assertTrue(hasattr(u1, "first_name"))
        self.assertTrue(hasattr(u1, "last_name"))

    def test_init_custom_args(self):
        """instantiation test of it's own  arguments"""
        u1a = User()
        self.assertEqual(isinstance(u1a, User), True)
        self.assertEqual(u1a.email, "")
        self.assertEqual(u1a.first_name, "")
        self.assertEqual(u1a.last_name, "")
        u1a.first_name = "Dola"
        self.assertEqual(u1a.first_name, "Dola")

    def test_init_with_args(self):
        """tests instantiation of object with arguments from dictionary"""
        dict1 = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                 'created_at': '2017-09-28T21:03:54.052298',
                 '__class__': 'User',
                 'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302',
                 'name': 'My_First_Model'}
        u2 = User(**dict1)
        self.assertTrue(hasattr(u2, "created_at"))
        self.assertIsInstance(u2.created_at, datetime)
        self.assertIsInstance(u2.updated_at, datetime)
        self.assertEqual(u2.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")


    def test_init_with_kwargs(self):
        """tests instantiation of object with direct kwargs"""
        u3 = User(id="78393",
                       created_at="2023-12-14T17:30:54.052298",
                       updated_at="2024-01-02T11:03:54.062721")
        self.assertEqual(type(u3.id), str)
        self.assertEqual(type(u3.created_at), datetime)


class TestUserMethods(unittest.TestCase):
    """ tests the methods of the `User` classs"""

    @patch('builtins.print')
    def test_str_method(self, mock_output):
        """checks that the output of `str()` matches the requirements"""
        u4 = User()
        u4.name = "first model"
        u4.number = "30"
        mod_str = f"[{u4.__class__.__name__}] ({u4.id}) {u4.__dict__}"
        output_of_str = str(u4)
        print(u4)
        self.assertEqual(output_of_str, mod_str)
        mock_output.assert_called_once_with(u4)

    def test_to_dict(self):
        """ checks that the output of `to_dict()` matches requirements"""
        u5 = User()
        u5.name = "new model"
        u5.number = 54
        mod_dict_str = u5.to_dict()
        self.assertEqual(type(mod_dict_str), dict)
        self.assertIn("User", u5.to_dict().values())
        self.assertIn("id", u5.to_dict().keys())
        self.assertEqual(type(mod_dict_str['created_at']), str)
        self.assertEqual(type(mod_dict_str['updated_at']), str)

    # def test_save(self):
    #     """checks that the updated_at attribute is updated with save() """
    #     u6 = User()
    #     # print(f"created at: {u6.created_at}")
    #     # print(f"update 0: {u6.updated_at}")
    #     self.assertAlmostEqual(u6.created_at, u6.updated_at,
    #                            delta=timedelta(seconds=1))
    #     u6.save()
    #     # print(f"update 1: {u6.updated_at}")
    #     self.assertNotAlmostEqual(u6.created_at, u6.updated_at,
    #                               delta=timedelta(microseconds=10))
    #     u6.save()
    #     # print(f"update 2: {u6.updated_at}")
    #     self.assertNotAlmostEqual(u6.created_at, u6.updated_at,
    #                               delta=timedelta(microseconds=1000))
