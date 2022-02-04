#!/usr/bin/python3
"""Doc stuff"""
import cmd, sys

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models import *


class HBNBCommand(cmd.Cmd):
    """Shell for AirBnB"""
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_quit(self, inp):
        "Exits the shell"
        return True

    def do_create(self, inp):
        "Creates a new instance of BaseModel, saves it \
(to the JSON file) and prints the id. Ex: $ create BaseModel"

        if inp == "":
            print("** class name missing **")
        else:
            try:
                class_model = globals()[inp]
                obj = class_model()
                obj.save()
                print(obj.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, inp):
        "Prints the string representation of an instance based \
on the class name and id. Ex: $ show BaseModel 1234-1234-1234"

        flag = 1
        if inp == "":
            print("** class name missing **")
            flag = 0
        else:
            inp = inp.split(" ")

        if flag == 1:
            if inp not in ("BaseModel", "User", "State", "Review", "Place", "City", "Amenity"):
                print("** class doesn't exist **")
            else:
                if len(inp) == 1:
                    print("** instance id missing **")
                else:
                    key = ".".join(inp)
                    objects = storage.all()
                    try:
                        print(objects[key])
                    except:
                        print("** no instance found **")

    def do_destroy(self, inp):
        "Deletes an instance based on the class name and id"

        flag = 1
        if inp == "":
            print("** class name missing **")
            flag = 0
        else:
            inp = inp.split(" ")

        if flag == 1:
            if inp not in ("BaseModel", "User", "State", "Review", "Place", "City", "Amenity"):
                print("** class doesn't exist **")
            else:
                if len(inp) == 1:
                    print("** instance id missing **")
                else:
                    key = ".".join(inp)
                    objects = storage.all()
                    try:
                        del(objects[key])
                        storage.save()
                    except:
                        print("** no instance found **")

    def do_all(self, inp):
        "Prints all string representation of all \
instances based or not on the class name."
        pass

    def do_update(self, inp):
        "Updates an instance based on the class \
name and id by adding or updating attribute"
        pass

    do_EOF = do_quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()