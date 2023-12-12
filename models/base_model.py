#!/usr/bin/python3
"""Defines a class Basemodel"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the airbnb."""

    def __init__(self, *args, **kwargs):
        """
        Initializes BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs for attributes.
        """
        formatter = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for a, b in kwargs.items():
                if a == "created_at" or a == "updated_at":
                    setattr(self, a, datetime.strptime(
                        b, formatter))
                elif a == "__class__":
                    continue
                else:
                    setattr(self, a, b)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def save(self):
        """Saves and updates the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Returns the dictionary of BaseModel instance.
        Including the key/value pair __class__ representing
        the class name.
        """
        empt_dict = {}
        for a, b in self.__dict__.items():
            if a == "created_at" or a == "updated_at":
                empt_dict[a] = datetime.isoformat(b)
            else:
                empt_dict[a] = b
        empt_dict["__class__"] = self.__class__.__name__
        return empt_dict
    
    def __str__(self):
        """Prints the string representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
