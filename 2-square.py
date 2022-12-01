#!/usr/bin/python3
""" Defines a class "Square" and its attributes """


class Square:
    """ defines a size of a square, which must be an integer """
    def __init__(self, size=0):
        """ instantiate with a size of integer data type

        Args:
            size: size of the square

        Return:
            Nothing
    """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
