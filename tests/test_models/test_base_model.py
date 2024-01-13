#!/usr/bin/python3
"""Test module for `BaseModel` class"""
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from io import StringIO
import sys
import uuid
from datetime import timedelta
from datetime import datetime



class TestBaseModel(unittest.TestCase):
    """ basic type-checking tests of attibutes in  the `BaseModel` class"""

    def test_types(self):
        """checks that the type of the object attributes
        are str and datetime"""
        mod1 = BaseModel()
        mod1_id = uuid.UUID(mod1.id)
        self.assertEqual(type(mod1_id), uuid.UUID)
        self.assertIsInstance(mod1.created_at, datetime)
        self.assertEqual(type(mod1.updated_at), type(mod1.updated_at))

    def test_uniqueness(self):
        """checks that ids are not the same"""
        mod2 = BaseModel()
        mod3 = BaseModel()
        self.assertNotEqual(mod2.id, mod3.id)


class TestBaseModelInstantiation(unittest.TestCase):
    """checks that the instantiation of `BaseModel` objects
    works correctly in various scenarios"""

    def test_init_no_args(self):
        """instantiation test with no arguments"""
        t1 = BaseModel()
        self.assertEqual(isinstance(t1, BaseModel), True)
        self.assertTrue(hasattr(t1, "created_at"))
        self.assertTrue(hasattr(t1, "updated_at"))
        self.assertTrue(hasattr(t1, "id"))
        self.assertAlmostEqual(t1.created_at, t1.updated_at,
                               delta=timedelta(seconds=1))

    def test_init_with_args(self):
        """tests instantiation of object with arguments from dictionary"""
        dict1 = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                 'created_at': '2017-09-28T21:03:54.052298',
                 '__class__': 'BaseModel',
                 'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302',
                 'name': 'My_First_Model'}
        mod3 = BaseModel(**dict1)
        self.assertTrue(hasattr(mod3, "created_at"))
        self.assertTrue(isinstance(mod3.created_at, datetime))
        self.assertTrue(isinstance(mod3.updated_at, datetime))
        self.assertEqual(mod3.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")

    def test_init_many_args(self):
        pass

    def test_init_with_kwargs(self):
        """tests instantiation of object with direct kwargs"""
        t2 = BaseModel(id="78393",
                       created_at="2023-12-14T17:30:54.052298",
                       updated_at="2024-01-02T11:03:54.062721")
        self.assertEqual(type(t2.id), str)
        self.assertTrue(isinstance(t2.created_at, datetime))


class TestBaseModelMethods(unittest.TestCase):
    """ tests the methods of the `BaseModel` classs"""

    @patch('builtins.print')
    def test_str_method(self, mock_output):
        """checks that the output of `str()` matches the requirements"""
        mod1 = BaseModel()
        mod1.name = "first model"
        mod1.number = "30"
        mod_str = f"[{mod1.__class__.__name__}] ({mod1.id}) {mod1.__dict__}"
        output_of_str = str(mod1)
        print(mod1)
        self.assertEqual(output_of_str, mod_str)
        mock_output.assert_called_once_with(mod1)

    def test_to_dict(self):
        """ checks that the output of `to_dict()` matches requirements"""
        mod2 = BaseModel()
        mod2.name = "new model"
        mod2.number = 54
        mod_dict_str = mod2.to_dict()
        self.assertEqual(type(mod_dict_str), dict)
        self.assertIn("BaseModel", mod2.to_dict().values())
        self.assertIn("id", mod2.to_dict().keys())
        self.assertEqual(type(mod_dict_str['created_at']), str)
        self.assertEqual(type(mod_dict_str['updated_at']), str)

    # def test_save(self):
    #     """checks that the updated_at attribute is updated with save() """
    #     t3 = BaseModel()
        # print(f"created at: {t3.created_at}")
        # print(f"update 0: {t3.updated_at}")
        # self.assertAlmostEqual(t3.created_at, t3.updated_at,
        #                        delta=timedelta(seconds=1))
        # t3.save()
        # print(f"update 1: {t3.updated_at}")
        # self.assertNotAlmostEqual(t3.created_at, t3.updated_at,
        #                           delta=timedelta(microseconds=10))
        # t3.save()
        # print(f"update 2: {t3.updated_at}")
        # self.assertNotAlmostEqual(t3.created_at, t3.updated_at,
        #                           delta=timedelta(microseconds=1000))


if "__name__" == "__main__":
    unittest.main()
