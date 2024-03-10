#!/usr/bin/env python3
"""Represents a class Place"""
from models.base_model import BaseModel

class Place(BaseModel):
    """
    Initaializes a class Place
    Attributes:
        city_id(str): the city's id
        user_id(str): the user's is
        name(str): the name of the place
        description(str): the place's description
        number_room(int): the number of rooms
        number_bathrooms(int): the no of bathrooms
        max_guest(int): the maximum no of guests
        price_by_night(int): the price charge per night
        latitude(float): the latitude direction
        longitude(float): the longitude direction
        amenity_ids(list): the id of the amenities
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_room = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
