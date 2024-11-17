#!/usr/bin/python3
"""
This mmodule contains unit tests for review
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Review class.
    """

    def test_no_args_instantiates(self):
        """
        Test that creating an instance of Review without arguments works.
        """
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        """
        Test that the new instance of Review is stored in the objects dictionary.
        """
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        """
        Test that the id attribute is a string.
        """
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        """
        Test that created_at attribute is a datetime object.
        """
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        """
        Test that updated_at attribute is a datetime object.
        """
        self.assertEqual(datetime, type(Review().updated_at))


class TestReview_save(unittest.TestCase):
    """
    Unittests for testing save method of the Review class.
    """

    @classmethod
    def setUp(self):
        """
        Prepare the environment before each test.
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
        rv = Review()
        sleep(0.05)
        first_updated_at = rv.updated_at
        rv.save()
        self.assertLess(first_updated_at, rv.updated_at)


class TestReview_to_dict(unittest.TestCase):
    """
    Unittests for testing to_dict method of the Review class.
    """

    def test_to_dict_type(self):
        """
        Test that to_dict returns a dictionary.
        """
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """
        Test that to_dict contains the correct keys.
        """
        rv = Review()
        self.assertIn("id", rv.to_dict())
        self.assertIn("created_at", rv.to_dict())
        self.assertIn("updated_at", rv.to_dict())
        self.assertIn("__class__", rv.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """
        Test that datetime attributes are converted to strings.
        """
        rv = Review()
        rv_dict = rv.to_dict()
        self.assertEqual(str, type(rv_dict["created_at"]))
        self.assertEqual(str, type(rv_dict["updated_at"]))

    def test_to_dict_output(self):
        """
        Test that to_dict returns a dictionary with the correct content.
        """
        dt = datetime.today()
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
        expected_dict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(rv.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()

