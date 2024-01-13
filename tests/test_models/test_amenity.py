#!/usr/bin/python3
"""test module for Amenity class"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from unittest.mock import patch
from io import StringIO
import sys
from datetime import timedelta
from datetime import datetime

class TestAmenity(unittest.TestCase):
    """ basic type-checking tests of attibutes in  the `Amenity` class"""

    def test_types(self):
        """confirm types of the custom argumenta"""
        am0a = Amenity()
        self.assertTrue(type(am0a.name), str)


    def test_subclass(self):
           """checks inheritance of `Amenity` objects"""
           am0 = Amenity()
           self.assertIsInstance(am0,Amenity)
           self.assertTrue(issubclass(type(am0),BaseModel))

class TestAmenityInstantiation(unittest.TestCase):
    """checks that the instantiation of `Amenity` objects
    works correctly in various scenarios"""

    def test_init_no_args(self):
        """instantiation test with no arguments"""
        am1 = Amenity()
        self.assertEqual(isinstance(am1, Amenity), True)
        self.assertTrue(hasattr(am1, "created_at"))
        self.assertTrue(hasattr(am1, "updated_at"))
        self.assertTrue(hasattr(am1, "id"))
        self.assertAlmostEqual(am1.created_at, am1.updated_at,
                               delta=timedelta(seconds=1))
        self.assertTrue(hasattr(am1, "name"))


    def test_init_custom_args(self):
        """instantiation test of it's own  arguments"""
        am1a = Amenity()
        self.assertEqual(isinstance(am1a, Amenity), True)
        self.assertEqual(am1a.name, "")
        am1a.name = "Wifi"
        self.assertEqual(am1a.name, "Wifi")

    def test_init_with_args(self):
        """tests instantiation of object with arguments from dictionary"""
        dict1 = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                 'created_at': '2017-09-28T21:03:54.052298',
                 '__class__': 'Amenity',
                 'updated_at': '2017-09-28T21:03:54.052302',
                 'name': 'Air Conditioning'}
        am2 = Amenity(**dict1)
        self.assertTrue(hasattr(am2, "created_at"))
        self.assertIsInstance(am2.created_at, datetime)
        self.assertIsInstance(am2.updated_at, datetime)
        self.assertEqual(am2.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")


    def test_init_with_kwargs(self):
        """tests instantiation of object with direct kwargs"""
        am3 = Amenity(id="78393",
                       created_at="2023-12-14T17:30:54.052298",
                       updated_at="2024-01-02T11:03:54.062721")
        self.assertEqual(type(am3.id), str)
        self.assertEqual(type(am3.created_at), datetime)
        print(am3.__dict__)

class TestAmenityMethods(unittest.TestCase):
    """ tests the methods of the `Amenity` classs"""

    @patch('builtins.print')
    def test_str_method(self, mock_output):
        """checks that the output of `str()` matches the requirements"""
        am4 = Amenity()
        am4.name = "first model"
        am4.number = "30"
        mod_str = f"[{am4.__class__.__name__}] ({am4.id}) {am4.__dict__}"
        output_of_str = str(am4)
        print(am4)
        self.assertEqual(output_of_str, mod_str)
        mock_output.assert_called_once_with(am4)

    def test_to_dict(self):
        """ checks that the output of `to_dict()` matches requirements"""
        am5 = Amenity()
        am5.name = "new model"
        am5.number = 54
        mod_dict_str = am5.to_dict()
        self.assertEqual(type(mod_dict_str), dict)
        self.assertIn("Amenity", am5.to_dict().values())
        self.assertIn("id", am5.to_dict().keys())
        self.assertEqual(type(mod_dict_str['created_at']), str)
        self.assertEqual(type(mod_dict_str['updated_at']), str)

    # def test_save(self):
    #     """checks that the updated_at attribute is updated with save() """
    #     am6 = Amenity()
    #     # print(f"created at: {am6.created_at}")
    #     # print(f"update 0: {am6.updated_at}")
    #     self.assertAlmostEqual(am6.created_at, am6.updated_at,
    #                            delta=timedelta(seconds=1))
    #     am6.save()
    #     # print(f"update 1: {am6.updated_at}")
    #     self.assertNotAlmostEqual(am6.created_at, am6.updated_at,
                                #   delta=timedelta(microseconds=10))
        # am6.save()
        # # print(f"update 2: {am6.updated_at}")
        # self.assertNotAlmostEqual(am6.created_at, am6.updated_at,
        #                           delta=timedelta(microseconds=1000))
