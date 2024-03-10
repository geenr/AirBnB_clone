#!/usr/bin/env python3
"""
Represents the BaseModel class which store all base classes and methods
to be used by all files.
"""
from datetime import datetime
import uuid
import models

class BaseModel:
    """
    Initialize the class BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        store all the methods which must be used by all files.
        Args:
            args: positional argument.
            kwargs: keyword argument.
        Atrributes:
            id(str): assigns uuid when an instance is created.
            created_at: assigns an instance current time when it is created.
            updated_at: updates an instance with current time after change in time.
        """

        format_iso = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, format_iso))
                else:
                    setattr(self, key, value)
        else:
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            self.id = str(uuid.uuid4())
        models.storage.new(self)

    def __str__(self):
        """
        prints the output in the following method below.
        """
        name_of_class = self.__class__.__name__
        return "[{}] ({}) {}".format(name_of_class, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance.
        """
        ob_dict = self.__dict__.copy()
        ob_dict['__class__'] = self.__class__.__name__
        ob_dict['created_at'] = self.created_at.isoformat()
        ob_dict['updated_at'] = self.updated_at.isoformat()
        return ob_dict

if __name__ == '__main__':
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
