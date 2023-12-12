#!/usr/bin/python
"""Defines a class State."""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents the state of the airbnb.

    Attribute:
        name (str): The name of the state.
    """
    
    name = ""
