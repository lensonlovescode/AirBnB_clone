#!/usr/bin/python3
"""
This module provides a command-line interpreter for managing
The Airbnb clone project. It allows users to create, show, update
and delete objects for various classes in the project
(such as `User`, `Place`, `State`, etc.).
"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
