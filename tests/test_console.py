#!/usr/bin/python3
""" Test module for the console"""
import unittest
from models.base_model import BaseModel
from models.user import User
import models
import sys
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import uuid
import json
from os import remove


def setUpModule():
    models.storage._FileStorage__objects.clear()


def tearDownModule():
    try:
        remove("file.json")
    except FileNotFoundError:
        pass
    models.storage._FileStorage__objects.clear()


class TestConsoleBasic(unittest.TestCase):
    """ tests basic functionalities of  the console"""

    @classmethod
    def setUpClass(self):
        self.console0 = HBNBCommand()

    @classmethod
    def tearDownClass(self):
        del self.console0

    def test_emptyline(self):
        """checks that inputing an emptyline or newline does nothing"""
        self.assertEqual(self.console0.onecmd(""), "")
        self.assertEqual(self.console0.onecmd("\n"), "")

    def test_quit_eof(self):
        """checks that quit and EOF exit the console"""
        self.assertEqual(self.console0.onecmd("EOF"), True)
        self.assertTrue(self.console0.onecmd("quit"))


class TestCreate(unittest.TestCase):
    """ tests `do_create()`
    Usage:
        create <classname>
    """
    @classmethod
    def setUpClass(self):
        self.console1 = HBNBCommand()

    @classmethod
    def tearDownClass(self):
        del self.console1

    def test_create_missing_class(self):
        """test create with a missing class"""
        expected = "** class name missing **"

        with patch("sys.stdout", new=StringIO()) as output:
            input_line = "create"
            self.console1.onecmd(input_line)
            self.assertEqual(expected, output.getvalue().strip())

    def test_create_wrong_class(self):
        """tests create with wrong class"""
        expected = "** class doesn't exist **"

        with patch("sys.stdout", new=StringIO()) as output:
            input_line = "create jog"
            self.console1.onecmd(input_line)
            self.assertEqual(expected, output.getvalue().strip())

    def test_create_succesful(self):
        """tests successful create command"""

        with patch("sys.stdout", new=StringIO()) as output:
            input_line = "create User"
            self.console1.onecmd(input_line)
            id_string = output.getvalue().strip()
            user_id = uuid.UUID(output.getvalue().strip())
            self.assertEqual(type(user_id), uuid.UUID)
            self.assertIn("User." + id_string, models.storage.all().keys())


class TestShow(unittest.TestCase):
    """tests do_show()
    Usage:
        show <classname> <id>
    """
    @classmethod
    def setUpClass(self):
        self.console2 = HBNBCommand()

    @classmethod
    def tearDownClass(self):
        del self.console2

    def test_show_no_class(self):
        """tests show with no arguments"""

        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            input_line = "show"
            self.console2.onecmd(input_line)
            self.assertEqual(expected, output.getvalue().strip())

    def test_no_id(self):
        """tests show with no id"""
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            input_line = "show User"
            self.console2.onecmd(input_line)
            self.assertEqual(expected, output.getvalue().strip())

    def test_show_wrong_class_or_id(self):
        """tests show with wrong class or id"""

        expected0 = "** class doesn't exist **"
        with patch("sys.stdout", new_callable=StringIO) as output:
            input_line = "show aUser"
            self.console2.onecmd(input_line)
            self.assertEqual(expected0, output.getvalue().strip())

        expected = "** no instance found **"
        with patch("sys.stdout", new_callable=StringIO) as output:
            input_line = "show User 12345"
            self.console2.onecmd(input_line)
            self.assertEqual(expected, output.getvalue().strip())

    def test_show_valid(self):
        """valid args to show command"""
        u1 = User()
        m1 = BaseModel()

        expected = str(u1)
        with patch("sys.stdout", new=StringIO()) as output:
            input_line = "show User " + u1.id
            self.console2.onecmd(input_line)
            self.assertEqual(expected, output.getvalue().strip())

        expected = str(m1)
        with patch("sys.stdout", new=StringIO()) as output:
            input_line = "show BaseModel " + m1.id
            self.console2.onecmd(input_line)
            self.assertEqual(expected, output.getvalue().strip())


class TestAll(unittest.TestCase):
    """ tests do_all()
    Usage:
        all or all <classname>
    """
    @classmethod
    def setUpClass(self):
        self.console3 = HBNBCommand()

    @classmethod
    def tearDownClass(self):
        del self.console3

    def test_all_no_args(self):
        """tests usage of all with no arguments"""
        models.storage.reload()
        with patch("sys.stdout", new_callable=StringIO) as output:
            all_input = "all"
            self.console3.onecmd(all_input)
            objs = output.getvalue().strip()
            objs_list = json.loads(objs)
            self.assertEqual(type(objs_list), list)
            self.assertEqual(type(objs[0]), str)
            self.assertEqual(type(objs[-1]), str)

    def test_all_classname(self):
        """tests all with classname argument"""
        models.storage.reload()
        with patch("sys.stdout", new_callable=StringIO) as output:
            all_input = "all User"
            self.console3.onecmd(all_input)
            users = output.getvalue().strip()
            user_list = json.loads(users)
            self.assertEqual(type(user_list), list)
            # Check this. I'm not sure why IndexError
            # self.assertEqual(user_list[0][1:5], "User")

    def test_all_failure(self):
        """tests all with wrong args"""
        models.storage.reload()
        expected0 = "** class doesn't exist **"
        with patch("sys.stdout", new_callable=StringIO) as output:
            all_input = "all Doors"
            self.console3.onecmd(all_input)
            self.assertEqual(expected0, output.getvalue().strip())
