#!/usr/bin/python3
"""
This module defines a class FileStorage that
serializes instances to a JSON file and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """
    This class serializes instances to
    a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return (FileStorage.__objects)

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        dict_objects = {key: value.to_dict() for
                        key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dumps(dict_objects, indent=4))

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised
        """

        try:
            with open(FileStorage.__file_path, 'r') as f:
                dict_objs = json.loads(f.read())
                for key, value_dict in dict_objs.items():
                    class_name = value_dict.pop('__class__')
                    obj = eval(f"{class_name}(**value_dict)")
                    self.new(obj)
        except FileNotFoundError:
            pass
