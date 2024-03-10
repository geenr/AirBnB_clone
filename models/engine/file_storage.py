#!/usr/bin/env python3
"""Represents the class FileStorage"""

from models.base_model import BaseModel
import json
import os
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """
    Initializing a class that serializes and deserializes JSON files.
    Attributes:
        __file_path(str): path to the JSON file.
        __objects(dict): dictionary that stores all object files.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the disctionary __objects."""
        return FileStorage.__objects 
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key_obj = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key_obj] = obj

    def save(self):
        """serializes the object files to JSON files."""
        new_dict = {}
        obj_files = FileStorage.__objects
        new_dict = {obj: obj_files[obj].to_dict() for obj in obj_files.keys()}
        with open(FileStorage.__file_path, "w") as a:
            json.dump(new_dict, a)

    def reload(self):
        """deserializes the JSON file only if the JSON file exists"""
        obj_path = FileStorage.__file_path
        if os.path.isfile(obj_path):
            with open(obj_path, "r", encoding="utf-8") as a:
                try:
                    new_dict = json.load(a)

                    for key, value in new_dict.items():
                        name_of_class, obj.id = key.split('.')

                        cls = eval(name_of_class)

                        instance = cls(**values)

                        obj_files = Filestorage.__objects
                        obj_files[key] = instance
                except Exception:
                    pass
