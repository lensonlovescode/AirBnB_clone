#!/usr/bin/python3
"""
This module defines a class User that inherits from BaseModel
It represents a user with the following public class attributes:
1. email: string
2. password: string
3. first_name: string
4. last_name: string
"""
import models


class User(models.base_model.BaseModel):
    """
    A class User that inherits from BaseModel
    It represents a user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
