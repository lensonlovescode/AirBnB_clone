#!/usr/bin/python3
"""
This module contains unittests for the state class
which also inherits from BaseModel
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the State class.
    """

    def test_no_args_instantiates(self):
        """
        Test that instantiating a State object with no arguments works.
        """
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        """
        Test that the new instance is stored in the objects dictionary.
        """
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_public_str(self):
        """
        Test that the id attribute is a string.
        """
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public_datetime(self):
        """
        Test that created_at attribute is a datetime object.
        """
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public_datetime(self):
        """
        Test that updated_at attribute is a datetime object.
        """
        self.assertEqual(datetime, type(State().updated_at))


class TestState_save(unittest.TestCase):
    """
    Unittests for testing save method of the State class.
    """

    @classmethod
    def setUp(self):
        """
        Set up before each test.
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """
        Clean up after each test.
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
        Test that save updates the updated_at attribute.
        """
        st = State()
        sleep(0.05)
        first_updated_at = st.updated_at
        st.save()
        self.assertLess(first_updated_at, st.updated_at)

    def test_two_saves(self):
        """
        Test that save updates updated_at multiple times.
        """
        st = State()
        sleep(0.05)
        first_updated_at = st.updated_at
        st.save()
        second_updated_at = st.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        st.save()
        self.assertLess(second_updated_at, st.updated_at)


class TestState_to_dict(unittest.TestCase):
    """
    Unittests for testing to_dict method of the State class.
    """

    def test_to_dict_type(self):
        """
        Test that to_dict returns a dictionary.
        """
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """
        Test that to_dict contains the correct keys.
        """
        st = State()
        self.assertIn("id", st.to_dict())
        self.assertIn("created_at", st.to_dict())
        self.assertIn("updated_at", st.to_dict())
        self.assertIn("__class__", st.to_dict())

    def test_to_dict_output(self):
        """
        Test that to_dict returns the correct dictionary.
        """
        dt = datetime.today()
        st = State()
        st.id = "123456"
        st.created_at = st.updated_at = dt
        expected_dict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(st.to_dict(), expected_dict)

    def test_contrast_to_dict_dunder_dict(self):
        """
        Test that to_dict and __dict__ return different values.
        """
        st = State()
        self.assertNotEqual(st.to_dict(), st.__dict__)

if __name__ == "__main__":
    unittest.main()

