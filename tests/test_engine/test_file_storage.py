#!/usr/bin/python3
""" Test module for 'FileStorage' class"""
import unittest
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import json


class TestFileStorageMethods(unittest.TestCase):
    """tests all methods of the `FileStorage` class"""

    def SetUp(self):
        """setup for this testcase"""

    def test_new(self):
        """checks that new() updates the __objects dictionary with
        new instances for all classes"""

        f1 = BaseModel()
        self.assertIn(f1.__class__.__name__ + "." + f1.id,
                      models.storage._FileStorage__objects)
        u1 = User()
        self.assertIn(u1.__class__.__name__ + "." + u1.id,
                      models.storage._FileStorage__objects)
        a1 = Amenity()
        self.assertIn(a1.__class__.__name__ + "." + a1.id,
                      models.storage.all().keys())

    def test_all(self):
        """checks that the correct object record is returned"""
        all_objs = models.storage.all()
        # print(all_objs)
        self.assertEqual(type(all_objs), dict)

    def test_save(self):
        """checks serialization process of instances in __objects"""
        m2 = BaseModel()
        a2 = Amenity()
        u2 = User()
        models.storage.save()

        with open("file.json", "r", encoding="utf-8") as file:
            recent_save = json.load(file)
            self.assertIn("BaseModel" + "." + m2.id, recent_save)

    def test_reload(self):
        """checks deserialization process of objects"""
        m3 = BaseModel()
        a3 = Amenity()
        u3 = User()
        models.storage.save()
        self.assertIn(u3.__class__.__name__ + "." + u3.id,
                      models.storage._FileStorage__objects)
        self.assertIn(m3.__class__.__name__ + "." + m3.id,
                      models.storage._FileStorage__objects)
        self.assertIn(a3.__class__.__name__ + "." + a3.id,
                      models.storage.all().keys())
        models.storage.reload()
        self.assertIn(u3.__class__.__name__ + "." + u3.id,
                      models.storage._FileStorage__objects)
        self.assertIn(m3.__class__.__name__ + "." + m3.id,
                      models.storage._FileStorage__objects)
        self.assertIn(a3.__class__.__name__ + "." + a3.id,
                      models.storage.all().keys())

if "__name__" == "__main__":
    unittest.main()
