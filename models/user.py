#!/usr/bin/env python3
"""Represents a class user"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    Initializes the class user.
    Attributes:
        email(str): User's email
        password(str): User's password
        first_name(str): User's first name
        last_name(str): User's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
