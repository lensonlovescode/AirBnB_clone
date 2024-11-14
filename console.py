#!/usr/bin/python3
"""
This module provides a command-line interpreter for managing
The Airbnb clone project. It allows users to create, show, update
and delete objects for various classes in the project
(such as `User`, `Place`, `State`, etc.).
"""
import cmd
from models.base_model import BaseModel


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
        try:
            obj = eval(f"{class_name}()")
            print(f"{obj.id}")
        except NameError as e:
            print("** class doesn't exist **")
            return
        obj.save
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
