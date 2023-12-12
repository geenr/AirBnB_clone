#!/usr/bin/python3
"""Defines the class Filestorage."""

import json
from models.amenity import Amenity
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.base_model import Basemodel
from models.review import Review

class FileStorage:
    """
    Represent an filestorage engine.

    Attributes:
        __file_path (str): File's name where the object is saved.
        __objects (dict): Dictionary for instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects
    
    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        objectClassName = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objectClassName, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        dict_obj = {obj: FileStorage.__objects[obj].to_dict() for obj in 
                    FileStorage.__objects.keys()}
        with open(FileStorage.__file_path, "w") as file_p:
            json.dump(dict_obj, file_p)
    
    def reload(self):
        """
        Deserializes the JSON file __file_path to __objects
        only if the JSON file exists ;
        otherwise, do nothing.
        If the file doesn’t
        exist, no exception should be raised
        """
        try:
            with open(FileStorage.__file_path) as path:
                objectDict = json.load(path)
                for j in objectDict.values():
                    cls_name = j["__class__"]
                    del j["__class__"]
                    self.new(eval(cls_name)(**j))
        except FileNotFoundError:
            return
