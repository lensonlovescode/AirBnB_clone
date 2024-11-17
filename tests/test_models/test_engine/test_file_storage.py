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
import os
import json
import unittest
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """
    Unit tests for the FileStorage class
    """

    @classmethod
    def setUp(self):
        """
        set up for ensuring file.json is handled correctly by all tests
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """
        teardown for ensuring file.json is handled correctly by all tests
        """
        try:
            os.remove("file.json")
        except IOError:
            pass  

    def test_all_empty(self):
        """
        Tests all() returns an empty dictionary when no objects are added
        """
        self.assertEqual(storage.all(), {})

    def test_all_not_empty(self):
        """
        Tests that __objects returns a non-empty dictionary when populated
        AKA when new() is called with an object
        """
        obj = BaseModel()
        self.assertEqual(len(storage.all()), 1)

    def test_all_with_arg(self):
        """
        Tests that a TypeError is raised when an argument is passed to all()
        """
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new_adds_objects(self):
        """
        Tests that new adds objects to the __objects dictionary
        and they exist with the correct keys
        """
        basemodel = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        storage.new(basemodel)
        storage.new(user)
        storage.new(state)
        storage.new(place)
        storage.new(city)
        storage.new(amenity)
        storage.new(review)

        self.assertIn("BaseModel." + basemodel.id, storage.all().keys())
        self.assertIn(basemodel, storage.all().values())
        self.assertIn("User." + user.id, storage.all().keys())
        self.assertIn(user, storage.all().values())
        self.assertIn("State." + state.id, storage.all().keys())
        self.assertIn(state, storage.all().values())
        self.assertIn("Place." + place.id, storage.all().keys())
        self.assertIn(place, storage.all().values())
        self.assertIn("City." + city.id, storage.all().keys())
        self.assertIn(city, storage.all().values())
        self.assertIn("Amenity." + amenity.id, storage.all().keys())
        self.assertIn(amenity, storage.all().values())
        self.assertIn("Review." + review.id, storage.all().keys())
        self.assertIn(review, storage.all().values())

    def test_new_invalid_object(self):
        """
        Tests that the new() method handles well invalid arguments
        such as a string object as an argument
        """
        with self.assertRaises(AttributeError):
            storage.new("Not an object")
        with self.assertRaises(AttributeError):
            storage.new(None)
        with self.assertRaises(AttributeError):
            storage.new(123)

    def test_save_serializes(self):
        """
        Tests that save serializes a dictionary correctly
        """
        basemodel = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()

        storage.new(basemodel)
        storage.new(user)
        storage.new(state)
        storage.new(place)
        storage.new(city)
        storage.new(amenity)
        storage.new(review)

        storage.save()

        with open("file.json", "r") as f:
            saved_data = json.load(f)

        self.assertIn("BaseModel." + basemodel.id, saved_data.keys())
        self.assertIn("User." + user.id, saved_data.keys())
        self.assertIn("State." + state.id, saved_data.keys())
        self.assertIn("Place." + place.id, saved_data.keys())
        self.assertIn("City." + city.id, saved_data.keys())
        self.assertIn("Amenity." + amenity.id, saved_data.keys())
        self.assertIn("Review." + review.id, saved_data.keys())

    def test_save_with_arguments(self):
        """
        Tests that save raises a TypeError when an argument is passed
        """
        base_model = BaseModel()
        with self.assertRaises(TypeError):
            storage.save('An argument')
    
    def test_reload_objects(self):
        """
        Tests that reload correctly loads objects
        """
        basemodel = BaseModel()
        user = User()
     
        storage.new(basemodel)
        storage.new(user)

        storage.save()

        new_storage = storage.__class__()
        new_storage.reload()

        self.assertIn("BaseModel." + basemodel.id, new_storage.all())
        self.assertIn("User." + user.id, new_storage.all())

        self.assertIn(basemodel.id, [obj.id for obj in new_storage.all().values()])
        self.assertIn(user.id, [obj.id for obj in new_storage.all().values()])

    def test_reload_nonexistent_file(self):
        """
        Tests that reload doesn't raise an exception: non-existent file
        """
        original_file_path = storage._FileStorage__file_path
        
        try:
            storage._FileStorage__file_path = 'non_existent_file.json'
            storage.reload()
        except Exception as e:
            self.fail(f"reload() raised {type(e).__name__} unexpectedly!")
        finally:
            storage._FileStorage__file_path = original_file_path
    def test_reload_with_arguments(self):
        """
        Test that calling reload() with arguments raises a TypeError
        """
        with self.assertRaises(TypeError):
            storage.reload('some_argument')


if __name__ == "__main__":
    unittest.main()
