#!/usr/bin/python
"""Defines a class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents the city of interest.

    Attributes:
        name (str): The city's name.
        state_id (str): The city's id/code.
    """
    
    state_id = ""
    name = ""
