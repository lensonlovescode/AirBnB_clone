#!/usr/bin/python3
"""
This module provides a command-line interpreter for managing
The Airbnb clone project. It allows users to create, show, update
and delete objects for various classes in the project
(such as `User`, `Place`, `State`, etc.).
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This class provides command-line interface commands to create, retrieve,
    update, and delete instances of classes within the Airbnb project.
    """
    prompt = "(hbnb)"
    valid_classes = ("BaseModel",
                     "User",
                     "Place",
                     "State",
                     "City",
                     "Amenity",
                     "Review"
                     )

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
        if class_name not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return

        obj = eval(f"{class_name}()")
        obj.save()
        print(f"{obj.id}")

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program once end of file.
        """
        print("")
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
        if len(args) < 2:
            print("** instance id missing **")
            return

        full_key = args[0] + "." + args[1]
        class_name = args[0]

        if class_name not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        objs = storage.all()

        obj = objs.get(full_key)

        if obj is None:
            print("** no instance found **")
            return
        print(obj.__str__())

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        Then saves the changes into the JSON file.
        Usage: destroy BaseModel 1234-1234-1234
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        class_name, obj_id = args
        if class_name not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return

        objs = storage.all()
        full_key = f"{class_name}.{obj_id}"
        if full_key not in objs:
            print("** no instance found **")
            return

        del objs[full_key]
        storage.save()

    def do_all(self, arg):
        """
        prints all string representation of all instances based or
        not on the class name.
        Usage: (hbnb) all BaseModel or (hbnb) all
        """
        args = arg.split()
        objs = storage.all()

        if args:
            class_name = args[0]
            if class_name not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
                return
            print(
                [
                    str(obj)
                    for key, obj in objs.items()
                    if key.startswith(class_name)
                ]
            )
        else:
            print([str(obj) for obj in objs.values()])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute,
        and saves the changes into the JSON file.
        Usage: (hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missinf **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        class_name, obj_id, attr_name, attr_value = args[:4]
        if class_name not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return

        objs = storage.all()
        full_key = f"{class_name}.{obj_id}"
        obj = objs.get(full_key)
        if obj is None:
            print("** no instance found **")
            return

        try:
            if attr_value.isdigit():
                attr_value = int(attr_value)
            elif '.' in attr_value:
                attr_value = float(attr_value)
            else:
                attr_value = attr_value.strip('"').strip("'")
        except ValueError:
            pass

        if attr_name not in ['id,' 'created_at', 'updated_at']:
            setattr(obj, attr_name, attr_value)
            obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
