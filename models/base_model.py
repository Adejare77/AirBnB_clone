#!/usr/bin/python3
"""BaseModel class definition"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """Defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs) -> None:
        """Class Constructor to instantiate parameters

        Args:
            args (optional): Not used
            kwargs (dict): arguments for the constructor of a BaseModel
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if (kwargs):
            # kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
            # '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.fromisoformat(kwargs['created_at'])
            kwargs['updated_at'] = datetime.fromisoformat(kwargs['updated_at'])
            self.__dict__.update(**kwargs)
            # for k, v in kwargs.items():
            #     setattr(self, k, v)
        else:
            models.storage.new(self)

    def __str__(self) -> str:
        """returns a __str__ representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """Updates the public instance attribute "updated_at" with
        current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """returns a dictionary containing all keys/values of __dict__
        of the instance"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        # dict_copy['created_at'] = datetime.isoformat(self.created_at)
        dict_copy['created_at'] = datetime.strftime(self.created_at,
                                                    "%Y-%m-%dT%H:%M:%S.%f")
        dict_copy['updated_at'] = datetime.isoformat(self.updated_at)
        return dict_copy
