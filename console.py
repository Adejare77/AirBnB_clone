#!/usr/bin/python3
"""The Console"""
import cmd
import re
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """creates a shell console for our models
    """
    prompt = "(hbnb) "
    __classes = ["Amenity", "BaseModel", "City", "Place", "Review",
                 "State", "User"]
    __all_objs = storage.all()

    def onecmd(self, line: str) -> bool:
        line = self.precmd(line)
        return super().onecmd(line)

    def emptyline(self) -> str:
        return ""

    def parse(self, line: str) -> list:
        """Splits line to args"""
        # Note. cmd is not given by the default parseline. Only args
        lines = re.findall(r'("[^"]*"|[A-Za-z0-9\._-]+|\{[^{}]+\})', line)
        # Ensures '"' are stripped if present
        lines = [args.strip('"') for args in lines]
        return lines

    def precmd(self, line: str) -> str:
        """method called before parseline method"""
        """precmd gives me control on cmd and args passed by me before
        returning to parseline() where I don't have control. So, the
        purpose of using 'precmd' is to manipulate Class.cmd(), else
        returns `line` to `parseline` exactly the way it received it
        """
        # encapsulate "..." as One and also ensures dictionaries are preserved
        lines = re.findall(r'("[^"]*"|[A-Za-z0-9\._-]+|\{[^{}]+\})', line)

        # Checks if we have Something like this: Model.cmd() in lines[0]
        if (lines and ("." in lines[0])):
            first_str = lines[0].split(".")
            # swap positions of Class and cmd
            first_str[0], first_str[1] = first_str[1], first_str[0]
            new_line_list = first_str + lines[1:]
            line = " ".join(new_line_list)
        return line

    def do_all(self, line) -> None:
        """prints all string representation of all instances based or not
on the class name
Usage:  all
        all()
        all <class name>
        all() <class name()>
        all <class name()>
        all() <class name>
        <class name>.all()
        <class name>.all
        """
        lines = self.parse(line)
        if (len(lines) == 0):
            objects = [k.__str__() for k in self.__all_objs.values()]
            print(objects)
        else:
            if (lines[0] in self.__classes):
                objects = [v.__str__() for k, v in self.__all_objs.items()
                           if k.split(".")[0] == lines[0]]
                print(objects)
            else:
                print("** class doesn't exist **")

    def do_count(self, line):
        """retrieve number of instances of a class in
command interpreter (console.py):
Usage:  count <class name>
        count() <class name()>
        count <class name()>
        count() <class name>
        <class name>.count()
        <class name>.count
        """
        lines = self.parse(line)
        if (len(lines) == 0):
            print("** class name missing **")
        elif (lines[0] in self.__classes):
            objects = [v.__str__() for k, v in self.__all_objs.items()
                       if k.split(".")[0] == lines[0]]
            print(len(objects))
        else:
            print("** class doesn't exist **")

    def do_create(self, line) -> None:
        """Creates a new instance of a given Class
(saves it to the JSON file and prints the id)
Usage:  create <class name>
        create() <class name()>
        create <class name()>
        create() <class name>
        <class name>.create()
        <class name>.create
        """
        lines = self.parse(line)
        if (len(lines) == 0):
            print("** class name missing **")
        elif (lines[0] not in self.__classes):
            print("** class doesn't exist **")
        else:
            obj = eval(lines[0])()
            print(obj.id)
            obj.save()
            self.__all_objs = storage.all()

    def do_destroy(self, line) -> None:
        """Deletes an instance based on the class name and id
(save the change into the JSON file)
Usage:  destroy <class name> <id>
        destroy() <class name()> <id>
        destroy <class name()> <id>
        destroy() <class name> <id>
        <class name>.destroy(<id>)
        <class name>.destroy(<id>)
        """
        lines = self.parse(line)
        if (len(lines) == 0):
            print("** class name missing **")
        elif (lines[0] not in self.__classes):
            print("** class doesn't exist **")
        elif (len(lines) == 1):
            print("** instance id missing **")
        else:
            cls_n_id = lines[0] + "." + lines[1]
            if cls_n_id not in self.__all_objs.keys():
                print("** no instance found **")
            else:
                del self.__all_objs[cls_n_id]
                self.__all_objs = storage.all()
                storage.save()

    def do_EOF(self, line) -> bool:
        """EOF signal to exit the program"""
        return True

    def do_quit(self, line) -> bool:
        """Quit command to exit the program"""
        return True

    def do_show(self, line) -> None:
        """prints the string representation of an instance
based on class name and id
Usage:  show <class name> <id>
        show() <class name()> <id>
        show <class name()> <id>
        show() <class name> <id>
        <class name>.show(<id>)
        <class name>.show(<id>)

        """
        lines = self.parse(line)
        if (len(lines) == 0):
            print("** class name missing **")
        elif (lines[0] not in self.__classes):
            print("** class doesn't exist **")
        elif (len(lines) == 1):
            print("** instance id missing **")
        else:
            cls_n_id = lines[0] + "." + lines[1]
            if cls_n_id not in self.__all_objs.keys():
                print("** no instance found **")
            else:
                print(self.__all_objs[cls_n_id])

    def do_update(self, line) -> None:
        """updates an instance based on the class name and id by adding
or updating attribute (save the change into the JSON file)
Usage:  update <class name> <id> <attribute name> "<attribute value>"
        update() <class name()> <id> <attribute name> "<attribute value>"
        update <class name()> <id> <attribute name> "<attribute value>"
        update() <class name> <id> <attribute name> "<attribute value>"
        <class name>.update(<id>, <attribute name>, "<attribute value>")
        <class name>.update(<id>, {"atrr1": "val1", "attr2": val2})
        """
        lines = self.parse(line)
        if (len(lines) == 0):
            print("** class name missing **")
        elif (lines[0] not in self.__classes):
            print("** class doesn't exist **")
        elif (len(lines) == 1):
            print("** instance id missing **")
        else:
            cls_n_id = lines[0] + "." + lines[1]
            if cls_n_id not in self.__all_objs.keys():
                print("** no instance found **")
            else:
                obj = self.__all_objs[cls_n_id]
                try:
                    dict_list = eval(lines[2])
                    obj.__dict__.update(**dict_list)
                    eval(lines[0]).save(obj)
                except Exception:
                    if (len(lines) == 2):
                        print("** attribute name missing **")
                    elif (len(lines) == 3):
                        print("** value missing **")
                    else:
                        try:
                            setattr(obj, lines[2], eval(lines[3]))
                        except NameError:
                            setattr(obj, lines[2], lines[3])
                        eval(lines[0]).save(obj)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
