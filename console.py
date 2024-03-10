#!/usr/bin/env python3
"""
Represents a class HBNBcommand which is used to access the console
"""
import cmd
import json
import uuid
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review

class HBNBcommand(cmd.Cmd):
    """
    Initialize a class HBNBcommand
    """
    intro = "hey welcome to my cmd"
    prompt = "(hbnb) "

    __class_name = ["BaseModel",
            "User",
            "City",
            "Place",
            "State",
            "Amenity",
            "Review"]

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """also quits the program"""
        return True

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        
        in_put = line.split()
        base_model = BaseModel()
        if len(in_put) == 0:
            print("** class name missing **")
        elif in_put[0] not in HBNBcommand.__class_name:
            print("** class doesn't exist **")
            
        elif len(in_put) < 2:
            print("** instance id missing **")
        else:
            all_obj = storage.all()
            key_obj = "{}.{}".format(in_put[0], in_put[1])
            if key_obj in all_obj:
                print(all_obj[key_obj])
            else:
                print("** no instance found **")

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        base_model = BaseModel()
        
        in_put = line.split()
        if len(in_put) == 0:
            print("** class name missing **")
        elif in_put[0] not in HBNBcommand.__class_name:
            print("** class doesn't exist **")
        else:
            print("{}".format(base_model.id))
            storage.save()

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        in_put = line.split()
        base_model = BaseModel()
        if len(in_put) == 0:
            print("** class name missing **")
        elif in_put[0] not in HBNBcommand.__class_name:
            print("** class doesn't exist **")

        elif len(in_put) < 2:
            print("** instance id missing **")
        else:
            all_obj = storage.all()
            key_obj = "{}.{}".format(in_put[0], in_put[1])
            if key_obj in all_obj:
                del all_obj[key_obj]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name"""
        in_put = line.split()
        all_obj = storage.all()
        if len(in_put) > 0 and in_put[0] not in HBNBcommand.__class_name:
            print("** class doesn't exist **")

        elif len(in_put) == 0:
            for key, value in all_obj.items():
                print(str(value))
        
        else:
            for key, value in all_obj.items():
                if key.split('.')[0] == in_put[0]:
                    print(str(value))

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)
        """
        in_put = line.split()
        base_model = BaseModel()
        if len(in_put) == 0:
            print("** class name missing **")
        elif in_put[0] not in HBNBcommand.__class_name:
            print("** class doesn't exist **")

        elif len(in_put) < 2:
            print("** instance id missing **")
        else:
            all_obj = storage.all()
            key_obj = "{}.{}".format(in_put[0], in_put[1])
            if key_obj not in all_obj:
                print("** no instance found **")
            elif len(in_put) < 3:
                print("** attribute name missing **")
            elif len(in_put) < 4:
                print("** value missing **")
            else:
                inst_obj = all_obj[key_obj]

                attribute_name = in_put[2]
                attribute_val = in_put[3]
                try:
                    atrribute_val = eval(attribute_val)
                except Exception:
                    pass
                setattr(inst_obj, attribute_name, attribute_val)

                inst_obj.save()

if __name__ == '__main__':
    HBNBcommand().cmdloop()
