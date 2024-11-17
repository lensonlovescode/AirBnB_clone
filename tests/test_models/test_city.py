#!/usr/bin/python3
"""
This module contains Unit tests for the City model.
"""
import unittest
from models.city import City


class TestCityModel(unittest.TestCase):
    """
    Unit tests for the City class.
    """

    def setUp(self):
        """
        Set up resources for testing
        """
        self.city = City()

    def test_attributes_exist(self):
        """
        Tests that the City object has the required attributes
        """
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "state_id"))

    def test_attribute_types(self):
        """
        Tests that the types of the attributes are correct
        """
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.state_id, str)

    def test_no_args_instantiates(self):
        """
        Tests instantiation with no arguments
        """
        self.assertEqual(type(self.city), City)

    def test_id_is_public_str(self):
        """
        Tests that id is a public string attribute
        """
        self.assertEqual(type(self.city.id), str)

    def test_state_id_is_public_class_attribute(self):
        """
        Test that state_id is a public class attribute
        """
        self.assertIn("state_id", dir(self.city))
        self.assertNotIn("state_id", self.city.__dict__)
        self.assertEqual(type(City.state_id), str)

    def test_name_is_public_class_attribute(self):
        """
        Test that name is a public class attribute
        """
        self.assertIn("name", dir(self.city))
        self.assertNotIn("name", self.city.__dict__)
        self.assertEqual(type(City.name), str)

    def test_two_cities_unique_ids(self):
        """
        Test that two City instances have unique ids
        """
        city_1 = City()
        city_2 = City()
        self.assertNotEqual(city_1.id, city_2.id)

    def test_str_method(self):
        """
        Tests the string representation (__str__) method
        """
        city_str = str(self.city)
        self.assertIn("[City]", city_str)
        self.assertIn(self.city.id, city_str)

    def test_to_dict_method(self):
        """
        Test the to_dict method of the City class
        """
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertIn("id", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertEqual(city_dict["__class__"], "City")

    def test_class_documentation(self):
        """
        Test if the City class is documented
        """
        self.assertIsNotNone(City.__doc__)


if __name__ == "__main__":
    unittest.main()

