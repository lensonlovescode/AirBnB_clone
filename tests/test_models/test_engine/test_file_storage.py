#!/usr/bin/python3
"""
This module contains unit tests for the file storage class which
serializes instances to a JSON file and deserializes JSON file to instances
tests include:
    1. Test for all(self) which returns the dictionary
    2. Tests for new(self, obj) which sets a dictionary key/value pairs
       key <obj class name>.id
    3. Tests for save(self) that serializes a dictionary to the JSON file
       (path: __file_path)
    4. Tests for reload(self) which deserializes the JSON file to a dictionary
       from the file defined in __file_path If the file doesn’t exist
       no exception should be raised)
"""
import unittest


class TestFileStorage(unittest.TestCase):
"""
Unit tests for the FileStorage class
"""
    pass
