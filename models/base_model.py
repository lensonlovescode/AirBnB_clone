#!/usr/bin/python3
"""
This module defines a class BaseModel that defines
all common attributes/methods for other classes
"""
from datetime import datetime


class BaseModel():
    """
    This class defines all common attributes/methods for other classes
    """
    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing
        all keys/values of __dict__ of the instance
        """
        dict_rep = {key:value for key, value in self.__dict__.items()}

        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return (dict_rep)

