#!/usr/bin/python3
"""
This module defines a state class that inherits from BaseModel
It represents a state in the system.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel.
    """
    name = ""
