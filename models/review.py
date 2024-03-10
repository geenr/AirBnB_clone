#!/usr/bin/env python3
"""Represents a class Review"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    Initializes a class Review
    Attributes:
        place_id(str): the place id involved
        user_id(str): the user writing the review
        text(str): the review notes
    """
    place_id = ""
    user_id = ""
    text = ""
