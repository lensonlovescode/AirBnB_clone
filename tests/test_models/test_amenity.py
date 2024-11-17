#!/usr/bin/python3
"""
This module contains Unit tests for the Amenity model
which inherits from BaseModel
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Unit tests for the Amenity class
    """

    def setUp(self):
        """
        Set up method
        """
        self.test_amenity = Amenity()

    def tearDown(self):
        """
        Tear down method for amenity tests
        """
        del self.test_amenity

    def test_has_name_attribute(self):
        """
        Tests if the Amenity instance has a name attribute
        """
        self.assertTrue(hasattr(self.test_amenity, "name"))

    def test_name_attribute_type(self):
        """
        Tests that the name attribute is a string
        """
        self.assertIsInstance(self.test_amenity.name, str)

    def test_str_representation(self):
        """
        Ensures that the __str__ method returns the correct format
        """
        amenity_str = self.test_amenity.__str__()
        self.assertIsNotNone(amenity_str)
        self.assertIn("[Amenity]", amenity_str)

    def test_to_dict_conversion(self):
        """
        Tests correctness of the to_dict method's output
        """
        amenity_dict = self.test_amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn("id", amenity_dict)
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")

    def test_class_has_docstring(self):
        """
        Tests if the Amenity class has documentation
        """
        self.assertTrue(isinstance(Amenity.__doc__, str))

    def test_module_has_docstring(self):
        """
        Verifies the amenity module has documentation
        """
        self.assertIsNotNone(Amenity.__module__.__doc__)

    def test_test_class_has_docstring(self):
        """
        Ensures the test class has documentation
        """
        self.assertIsNotNone(self.__class__.__doc__)


if __name__ == "__main__":
    unittest.main()

