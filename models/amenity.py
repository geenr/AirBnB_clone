#!/usr/bin/python3
"""Define the class Amenity"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Represents amenities with their names

    Attributes:
        name (str): The amenity's name.
    """

    name = ""
