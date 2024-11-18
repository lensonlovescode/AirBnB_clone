#!/usr/bin/python3
"""
This is a unittest module for console.py
"""
import sys
import os
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User

class TestHBNBCommand(unittest.TestCase):
    """
    Unittest for the HBNBCommand class.
    """

    def setUp(self):
        """
        Setup resources for testing.
        """
        storage.all().clear()
        storage.save()

    def test_create_with_valid_class(self):
        """
        Tests create command with a valid class.
        """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = output.getvalue().strip()
            self.assertIn("BaseModel." + obj_id, storage.all())

    def test_create_with_invalid_class(self):
        """
        Test create command with no class provided
        """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create InvalidClass")
            self.assertEqual(output.getvalue().strip(), "** class doesn't exist **")

    def test_create_with_no_class(self):
        """
        Test create command where no class is provided.
        """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create")
            self.assertEqual(output.getvalue().strip(), "** class name missing **")

    def test_show_with_valid_id(self):
        """
        Test show command with a valid class and id,
        """
        obj =BaseModel()
        obj.save()
        obj_id = obj.id
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f"show BaseModel {obj_id}")
            self.assertIn(obj_id, output.getvalue().strip())

    def test_show_with_invalid_id(self):
        """
        Test show command with a valid class but invalid id.
        """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("show BaseModel invalid_id")
            self.assertEqual(output.getvalue().strip(), "** no instance found **")

    def test_show_with_no_class(self):
        """
        Test show command with no class provided.
        """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("show")
            self.assertEqual(output.getvalue().strip(), "** class name missing **")

    def test_quit(self):
        """
        Testing quit command to ensure it returns True and exits.
        """
        result = HBNBCommand().do_quit(None)
        self.assertTrue(result)

    def test_EOF(self):
        """
        Test EOF command to ensure it returns True and exits.
        """
        result = HBNBCommand().do_EOF(None)
        self.assertTrue(result)

    def test_emptyline(self):
        """
        Tests that an empty line does nothing
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            cmd = HBNBCommand()
            cmd.emptyline()
            self.assertEqual(mock_stdout.getvalue(), "")

    def test_destroy_with_valid_id(self):
        """
        Test destroy command with a valid class and id.
        """
        obj = User()
        obj.save()
        obj_id = obj.id
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f"destroy User {obj_id}")
            storage.save()
            self.assertNotIn(f"User.{obj_id}", storage.all())

    def test_destroy_with_invalid_id(self):
        """
        Test destroy command with a valid class but invalid id.
        """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("destroy BaseModel invalid_id")
            self.assertEqual(output.getvalue().strip(), "** no instance found **")

    def test_all_with_valid_class(self):
        """
        Test all command with a valid class.
        """
        obj1 = BaseModel()
        obj1.save()
        obj2 = BaseModel()
        obj2.save()
        with patch("sys.stdout", new=StringIO()) as output:
           HBNBCommand().onecmd("all BaseModel")
           self.assertIn(str(obj1), output.getvalue())
           self.assertIn(str(obj2), output.getvalue())

    def test_all_without_class(self):
        """
        Test all command without specifying a class.
        """
        obj1 = BaseModel()
        obj1.save()
        obj2 = User()
        obj2.save()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all")
            self.assertIn(str(obj1), output.getvalue())
            self.assertIn(str(obj2), output.getvalue())

    def test_update_with_valid_data(self):
        """
        Test update command with valid data.
        """
        obj = BaseModel()
        obj.save()
        obj_id = obj.id
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(f'update BaseModel {obj_id} name "TestName"')
            self.assertEqual(storage.all()[f"BaseModel.{obj_id}"].name, "TestName")
    

if __name__ == "__main__":
     unittest.main()
