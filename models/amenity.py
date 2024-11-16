#!/usr/bin/python3
"""
Module that defines a class that inherits from BaseModel.
It represents an amenity available at a place.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel
    """
    name = ""
