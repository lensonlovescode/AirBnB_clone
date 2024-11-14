#!/usr/bin/python3
"""
This module provides a command-line interpreter for managing
The Airbnb clone project. It allows users to create, show, update
and delete objects for various classes in the project
(such as `User`, `Place`, `State`, etc.).
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This class provides command-line interface commands to create, retrieve,
    update, and delete instances of classes within the Airbnb project.
    """
    prompt = "(hbnb) "

    def do_greet(self, arg):
        """
        Creates a new instance of a given class and saves it.
        """
        print("Hi!")

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        and saves in the JSON file
        Usage: (hbnb) create BaseModel
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]
        valid_classes = ["BaseModel"]

        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return

        obj = eval(f"{class_name}()")
        obj.save()
        print(f"{obj.id}")

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program once end of file.
        """
        return True

    def emptyline(self):
        """
        Override the default behaviour of executing the last command
        when an empty line is entered.
        """
        pass
    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        Usage: show BaseModel 1234-1234-1234.
        """
        args = arg.split()

        if len(args) < 1:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        valid_classes = ["BaseModel"]
        full_key = args[0] + "." + args[1]
        class_name = args[0]

        if class_name not in valid_classes:
            print("** class doesn't exist **")
            return
        objs = storage.all()

        obj = objs.get(full_key)

        if obj is None:
            print("** no instance found **")
            return
        print(obj.__str__())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
