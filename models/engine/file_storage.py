#!/usr/bin/python3
"""File Storage Type (JSON)"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """serializes instances to a JSON file and deserializes
    JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """returns the dictionary '__objects'"""
        return self.__objects

    def new(self, obj) -> None:
        """sets in '__objects' the "obj" with key "<obj class name>.id"

        Args:
            obj (dict): dictionary representing an instance
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self) -> None:
        """serializes '__objects' to the JSON file (path: __file_path)"""
        new_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as w_file:
            json.dump(new_dict, w_file)

    def reload(self) -> None:
        """deserializes the JSON file to '__objects' (only if the JSON
        file (__file_path) exist; otherwise, do nothing. If the file
        doesn't exist, no exception should be raised)"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                r_file = json.load(file)
                for obj, v in r_file.items():
                    _cls = v['__class__']
                    del v['__class__']
                    self.new(eval(_cls)(**v))
        except FileNotFoundError:
            pass
