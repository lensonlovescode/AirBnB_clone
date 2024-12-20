#!/usr/bin/python3
"""
This module contains unit tests for the base class
"""
import os
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Unittests for the BaseModel class
    """

    def test_instantiation(self):
        """
        Tests that a BaseModel instance is created correctly
        """
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)

    def test_save_updates_updated_at(self):
        """
        Tests that calling save updates the updated_at attribute
        """
        bm = BaseModel()
        old_updated_at = bm.updated_at
        sleep(0.05)
        bm.save()
        self.assertNotEqual(old_updated_at, bm.updated_at)

    def test_to_dict(self):
        """
        Tests that to_dict converts the object to a dictionary
        """
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(type(bm_dict), dict)
        self.assertEqual(bm_dict['__class__'], 'BaseModel')

    def test_save_creates_file(self):
        """
        Tests that a file is created after calling save
        """
        bm = BaseModel()
        bm.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_no_kwargs(self):
        """
        Tests that BaseModel can be instantiated without kwargs
        """
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
 
    def test_add_attrs_after_instantiation(self):
        """
        Tests that new attributes can be added after instantiation
        """
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 98
        self.assertEqual(bm.name, "Holberton")
        self.assertEqual(bm.my_number, 98)

    def test_no_file_deleted_after_save(self):
        """
        Tests that file.json is not deleted after calling save
        """
        bm = BaseModel()
        bm.save()
        bm2 = BaseModel()
        bm2.save()
        self.assertTrue(os.path.exists("file.json"))

if __name__ == "__main__":
    unittest.main()

