#!/usr/bin/python3
"""
Module that defines a City class  that inherits from BaseModel
It represents a city within a state.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel
    """
    state_id = ""
    name = ""
