#!/usr/bin/env python3
"""Represents a class City"""
from models.base_model import BaseModel

class City(BaseModel):
    """
    Intitalize the class City
    Attributes:
        state_id(str): the id of the state
        name(str): the name of the city
    """
    state_id = ""
    name = ""
