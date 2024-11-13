#!/usr/bin/python3
"""
This module defines all common attributes and methods for other classes
i.e;
each instance of the BaseModel has a unique ID ,
a creation timestamp
and an update timestamp.
The str method ensures a consistent string
representation of instances while the save method allows for
keeping track of the last modification.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    Defines all common attributes or methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance with
        a unique id (which is generated as a string),
        created_at(keeps record of the creation time),
        and updated_at(which is then set to creation time).
        If kwargs is provided, it should create an instance
        attribute from the key-value pairs. Otherwise,
        it should generate a new ID and set created_at and updated_at.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, value)
                else:
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

    def to_dict(self):
        """
        Returns a dictionary that contains all keys or values
        of __dict__ of the instance, with created_at and
        updated_at converted to strings in ISO format.
        """
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        return dict_rep
