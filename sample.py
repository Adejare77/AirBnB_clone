#!/usr/bin/env python3

import cmd
import turtle

class Hbnb(cmd.Cmd):
    intro = "Welcome home Rashisky"
    prompt = "(hbnb) "

    def do_quit(self):

