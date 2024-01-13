#!/usr/bin/python3
"""test module for State class"""
import unittest
from models.state import State
from models.base_model import BaseModel
from unittest.mock import patch
from io import StringIO
import sys
from datetime import timedelta
from datetime import datetime

class TestState(unittest.TestCase):
    """ basic type-checking tests of attibutes in  the `State` class"""

    def test_types(self):
        """confirm types of the custom argumenta"""
        s0a = State()
        self.assertTrue(type(s0a.name), str)


    def test_subclass(self):
           """checks inheritance of `State` objects"""
           s0 = State()
           self.assertIsInstance(s0,State)
           self.assertTrue(issubclass(type(s0),BaseModel))

class TestStateInstantiation(unittest.TestCase):
    """checks that the instantiation of `State` objects
    works correctly in various scenarios"""

    def test_init_no_args(self):
        """instantiation test with no arguments"""
        s1 = State()
        self.assertEqual(isinstance(s1, State), True)
        self.assertTrue(hasattr(s1, "created_at"))
        self.assertTrue(hasattr(s1, "updated_at"))
        self.assertTrue(hasattr(s1, "id"))
        self.assertAlmostEqual(s1.created_at, s1.updated_at,
                               delta=timedelta(seconds=1))
        self.assertTrue(hasattr(s1, "name"))


    def test_init_custom_args(self):
        """instantiation test of it's own  arguments"""
        s1a = State()
        self.assertEqual(s1a.name, "")
        s1a.name = "Niger"
        self.assertEqual(s1a.name, "Niger")

    def test_init_with_args(self):
        """tests instantiation of object with arguments from dictionary"""
        dict1 = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                 'created_at': '2017-09-28T21:03:54.052298',
                 '__class__': 'State',
                 'updated_at': '2017-09-28T21:03:54.052302',
                 'name': 'Kebbi'}
        s2 = State(**dict1)
        self.assertTrue(hasattr(s2, "created_at"))
        self.assertIsInstance(s2.created_at, datetime)
        self.assertIsInstance(s2.updated_at, datetime)
        self.assertEqual(s2.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")


    def test_init_with_kwargs(self):
        """tests instantiation of object with direct kwargs"""
        s3 = State(id="78393",
                       created_at="2023-12-14T17:30:54.052298",
                       updated_at="2024-01-02T11:03:54.062721")
        self.assertEqual(type(s3.id), str)
        self.assertEqual(type(s3.created_at), datetime)


class TestStateMethods(unittest.TestCase):
    """ tests the methods of the `State` classs"""

    @patch('builtins.print')
    def test_str_method(self, mock_output):
        """checks that the output of `str()` matches the requirements"""
        s4 = State()
        s4.name = "first model"
        s4.number = "30"
        mod_str = f"[{s4.__class__.__name__}] ({s4.id}) {s4.__dict__}"
        output_of_str = str(s4)
        print(s4)
        self.assertEqual(output_of_str, mod_str)
        mock_output.assert_called_once_with(s4)

    def test_to_dict(self):
        """ checks that the output of `to_dict()` matches requirements"""
        s5 = State()
        s5.name = "new model"
        s5.number = 54
        mod_dict_str = s5.to_dict()
        self.assertEqual(type(mod_dict_str), dict)
        self.assertIn("State", s5.to_dict().values())
        self.assertIn("id", s5.to_dict().keys())
        self.assertEqual(type(mod_dict_str['created_at']), str)
        self.assertEqual(type(mod_dict_str['updated_at']), str)

    # def test_save(self):
    #     """checks that the updated_at attribute is updated with save() """
    #     s6 = State()
    #     # print(f"created at: {s6.created_at}")
    #     # print(f"update 0: {s6.updated_at}")
    #     self.assertAlmostEqual(s6.created_at, s6.updated_at,
    #                            delta=timedelta(seconds=1))
    #     s6.save()
    #     # print(f"update 1: {s6.updated_at}")
    #     self.assertNotAlmostEqual(s6.created_at, s6.updated_at,
    #                               delta=timedelta(microseconds=10))
    #     s6.save()
    #     # print(f"update 2: {s6.updated_at}")
    #     self.assertNotAlmostEqual(s6.created_at, s6.updated_at,
    #                               delta=timedelta(microseconds=1000))
