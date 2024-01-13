#!/usr/bin/python3
import json
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage

class TestFileStorage_init(unittest.TestCase):
    """unittests for `FileStorage` instantiation"""

    def test_init_no_args(self):
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_init_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_path_is_private(self):
        with self.assertRaises(AttributeError):
            FileStorage.__file_path

    def test_file_path_is_private_str(self):
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_objects_is_private(self):
        with self.assertRaises(AttributeError):
            FileStorage.__file_path

    def test_objects_is_private_dict(self):
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_storage_init(self):
        self.assertEqual(type(storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """unittests for all FileStorage methods"""

    @classmethod
    def setUpClass(cls) -> None:
        # cls = FileStorage()
        # FileStorage.method(storage, ?) = storage.method(?)
        cls.storage = FileStorage()
        cls.am = Amenity()
        cls.bm = BaseModel()
        cls.ct = City()
        cls.pl = Place()
        cls.rv = Review()
        cls.st = State()
        cls.us = User()

    @classmethod
    def tearDownClass(cls) -> None:
        """clear any file.json created"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_all_type(self):
        """checks that the correct object record is returned"""
        self.assertEqual(type(FileStorage().all()), dict)

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage().all(None)

    def test_new_no_arg(self):
        with self.assertRaises(TypeError):
            FileStorage().new() # storage.new()

    def test_new_individual_instance(self):
        """checks that new() updates the __objects dictionary with
        new instances for all classes"""

        f1 = BaseModel()
        self.assertIn(f1.__class__.__name__ + "." + f1.id, storage._FileStorage__objects)
        u1 = User()
        self.assertIn(u1.__class__.__name__ + "." + u1.id, storage._FileStorage__objects)
        a1 = Amenity()
        self.assertIn(a1.__class__.__name__ + "." + a1.id, storage.all().keys())

    def test_new_with_args(self):
        self.storage.new(self.am)
        self.storage.new(self.bm)
        self.storage.new(self.ct)
        self.storage.new(self.pl)
        self.storage.new(self.rv)
        self.storage.new(self.st)
        self.storage.new(self.us)

        self.assertIn(self.am.__class__.__name__ + "." + self.am.id, self.storage.all().keys())
        self.assertIn(self.bm.__class__.__name__ + "." + self.bm.id, self.storage.all().keys())
        self.assertIn(self.ct.__class__.__name__ + "." + self.ct.id, self.storage.all().keys())
        self.assertIn(self.pl.__class__.__name__ + "." + self.pl.id, self.storage.all().keys())
        self.assertIn(self.rv.__class__.__name__ + "." + self.rv.id, self.storage.all().keys())
        self.assertIn(self.st.__class__.__name__ + "." + self.st.id, storage.all().keys())
        self.assertIn(self.us.__class__.__name__ + "." + self.us.id, self.storage.all().keys())

        self.assertIn(self.am, self.storage.all().values())
        self.assertIn(self.bm, self.storage.all().values())
        self.assertIn(self.ct, self.storage.all().values())
        self.assertIn(self.pl, self.storage.all().values())
        self.assertIn(self.rv, self.storage.all().values())
        self.assertIn(self.st, self.storage.all().values())
        self.assertIn(self.us, self.storage.all().values())

    def test_new_with_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            self.storage.new(User(), {"first_name": "Rashisky"})

    def test_save_with_no_args(self):
        self.storage.save()
        with open("file.json", "r", encoding="utf-8") as file:
            temp_file = json.load(file)

        self.assertIn(self.am.__class__.__name__ + "." + self.am.id, temp_file)
        self.assertIn(self.bm.__class__.__name__ + "." + self.bm.id, temp_file)
        self.assertIn(self.ct.__class__.__name__ + "." + self.ct.id, temp_file)
        self.assertIn(self.pl.__class__.__name__ + "." + self.pl.id, temp_file)
        self.assertIn(self.rv.__class__.__name__ + "." + self.rv.id, temp_file)
        self.assertIn(self.st.__class__.__name__ + "." + self.st.id, temp_file)
        self.assertIn(self.us.__class__.__name__ + "." + self.us.id, temp_file)

        self.assertIn(self.am.to_dict(), temp_file.values())
        self.assertIn(self.bm.to_dict(), temp_file.values())
        self.assertIn(self.ct.to_dict(), temp_file.values())
        self.assertIn(self.pl.to_dict(), temp_file.values())
        self.assertIn(self.rv.to_dict(), temp_file.values())
        self.assertIn(self.st.to_dict(), temp_file.values())
        self.assertIn(self.us.to_dict(), temp_file.values())

    def test_reload_with_no_args(self):
        self.storage.reload()
        objs = FileStorage._FileStorage__objects

        self.assertIn("Amenity." + self.am.id, objs)
        self.assertIn("BaseModel." + self.bm.id, objs)
        self.assertIn("City." + self.ct.id, objs)
        self.assertIn("Place." + self.pl.id, objs)
        self.assertIn("Review." + self.rv.id, objs)
        self.assertIn("State." + self.st.id, objs)
        self.assertIn("User." + self.us.id, objs)


if "__name__" == "__main__":
    unittest.main()
