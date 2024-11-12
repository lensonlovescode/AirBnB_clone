#!/usr/bin/python3
"""
This module defines all common attributes and methods for other classes
i.e; each instance of the BaseModel has a unique ID , a creation timestam
and an update timestamp.The str method ensures a consistent string
representation of instances while the save method allows for
keeping track of the last modification.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    Defines all common attributes or methods for other classes.
    """

    def __init__(self):
        """
        Initializes a new BaseModel instance with
        a unique id (which is generated as a string),
        created_at(keeps record of the creation time),
        and updated_at(which is then set to creation time).
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the instance.
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
