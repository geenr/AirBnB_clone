#!/usr/bin/python
"""Defines a class Place."""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents the Place of interest.

    Attributes:
        city_id (str): The city's code.
        name (str): The city's name.
        user_id (str): The user's id.
        description (str): the places details
        number_rooms (int): The number of rooms available.
        number_bathrooms (int): The number of bathrooms.
        max_guest (int): max no of guests accomodated.
        price_by_night (int): The price per night.
        latitude (float): The latitude coordinates.
        longitude (float): The longitude coordinates.
        amenity_ids (list): The amenity's id of each amenity.
    """
    
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
