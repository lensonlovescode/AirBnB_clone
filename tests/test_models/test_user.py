#!/usr/bin/python3
"""
This module contains unit tests for the class User
whhich inherits from BaseModel
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser(unittest.TestCase):
    """
    This class contains Unit tests for the User class
    """

    def test_type(self):
        """
        Tests that an instance of User is of type User
        """
        self.assertEqual(User, type(User()))

    def test_storage(self):
        """
        Tests that an instance of User is stored in the
        __objects dictionary when created
        """
        self.assertIn(User(), models.storage.all().values())

    def test_id(self):
        """
        Tests that the id attribute is a string
        """
        self.assertEqual(str, type(User().id))

    def test_datetime(self):
        """
        Tests that the attribute created_at and updated_at are
        of type datetime
        """
        self.assertEqual(datetime, type(User().created_at))
        self.assertEqual(datetime, type(User().updated_at))

    def test_email(self):
        """
        Tests that the email attribute is a public string
        """
        self.assertEqual(str, type(User.email))

    def test_password(self):
        """
        Tests that the user attribute is a public string
        """
        self.assertEqual(str, type(User.password))

    def test_name(self):
        """
        Tests that the attributes first_name and last_name are
        public strings
        """
        self.assertEqual(str, type(User.first_name))
        self.assertEqual(str, type(User.last_name))


    def test_unique_id(self):
        """
        Tests that a unique id is always assigned to an instance
        """
        us1 = User()
        us2 = User()
        self.assertNotEqual(us1.id, us2.id)

    def test_time(self):
        """
        Tests that created_at and updated_at attributes
        are assigned the current time correctly
        """
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.created_at, us2.created_at)

        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_args_unused(self):
        """
        Tests that unused arguments are ignored during instantiation.
        """
        user = User(None)
        self.assertNotIn(None, user.__dict__.values())

    def test_str_representation(self):
        """
        Tests the string representation of a User instance.
        """
        dt = datetime.today()
        dt_repr = repr(dt)
        user = User()
        user.id = "123456"
        user.created_at = user.updated_at = dt
        user_str = user.__str__()
        self.assertIn("[User] (123456)", user_str)
        self.assertIn("'id': '123456'", user_str)
        self.assertIn("'created_at': " + dt_repr, user_str)
        self.assertIn("'updated_at': " + dt_repr, user_str)

    def test_instantiation_with_kwargs(self):
        """
        Tests instantiation with keyword arguments.
        """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        us = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(us.id, "345")
        self.assertEqual(us.created_at, dt)
        self.assertEqual(us.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """
        Tests that instantiation with None in kwargs raises a TypeError.
        """
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_to_dict(self):
        """
        Tests that to_dict returns a dictionary.
        """
        self.assertTrue(dict, type(User().to_dict()))


if __name__ == "__main__":
    unittest.main()
