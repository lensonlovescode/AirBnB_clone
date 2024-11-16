#!/usr/bin/python3
"""
Module that defines a Review class that inherits from BaseModel.
It represents a review for a place.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
