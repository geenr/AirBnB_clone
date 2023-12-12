#!/usr/bin/python
"""Defines a class Review."""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents the reviews given.

    Attributes:
        place_id (str): The id of the place rented.
        user_id (str): The user of the place.
        text (str): The comment given.
    """
    
    place_id = ""
    user_id = ""
    text = ""
