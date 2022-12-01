#!/usr/bin/python3
""" Defines a class "Square" and its attributes """


class Square:
    """ Defines the size of the square """
    def __init__(self, size):
        """ instantiate size to instance private attribute "size"

            Args:
                size: size of the square

            Return:
                nothing
        """
        self.__size = size
