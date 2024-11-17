#!/usr/bin/python3
"""
This module contains unit tests for place
which inherits from BaseMModel
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Place class
    """

    def test_no_args_instantiates(self):
        """
        Tests that a Place instance can be created without arguments.
        """
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        """
        Tests that a new Place instance is stored in models.storage.all().
        """
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        """
        Tests that id is a string.
        """
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        """
        Tests that created_at is a datetime object
        """
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        """
        Tests that 'updated_at is a datetime object
        """
        self.assertEqual(datetime, type(Place().updated_at))


class TestPlace_save(unittest.TestCase):
    """
    Unittests for testing save method of the Place class
    """

    @classmethod
    def setUp(self):
        """
        Prepare the environment before each test
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """
        Restore the environment after each test
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """
        Test that updated_at changes after calling save()
        """
        pl = Place()
        sleep(0.05)
        first_updated_at = pl.updated_at
        pl.save()
        self.assertLess(first_updated_at, pl.updated_at)

    def test_two_saves(self):
        """
        Test that calling save() multiple times updates updated_at each time
        """
        pl = Place()
        sleep(0.05)
        first_updated_at = pl.updated_at
        pl.save()
        second_updated_at = pl.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        pl.save()
        self.assertLess(second_updated_at, pl.updated_at)


class TestPlace_to_dict(unittest.TestCase):
    """
    Unittests for testing to_dict method of the Place class
    """

    def test_to_dict_type(self):
        """
        Test that to_dict() returns a dictionary
        """
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """
        Test that to_dict() contains keys 'id', 'created_at'
        'updated_at', and '__class__'.
        """
        pl = Place()
        self.assertIn("id", pl.to_dict())
        self.assertIn("created_at", pl.to_dict())
        self.assertIn("updated_at", pl.to_dict())
        self.assertIn("__class__", pl.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """
        Tests that datetime attributes are converted to strings in to_dict()
        """
        pl = Place()
        pl_dict = pl.to_dict()
        self.assertEqual(str, type(pl_dict["created_at"]))
        self.assertEqual(str, type(pl_dict["updated_at"]))

    def test_to_dict_output(self):
        """
        Tests that to_dict() returns the expected dictionary format
        """
        dt = datetime.today()
        pl = Place()
        pl.id = "123456"
        pl.created_at = pl.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(pl.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """
        Test that the output of to_dict() is different from __dict__
        """
        pl = Place()
        self.assertNotEqual(pl.to_dict(), pl.__dict__)


if __name__ == "__main__":
    unittest.main()

