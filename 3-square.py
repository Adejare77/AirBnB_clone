#!/usr/bin/python3
""" Defines a class "Square" and its attributes """


class Square:
    """ defines a square whose data type must be an integer

        Args:
            size: size of the square

        Return:
            Area of the square
    """
    def __init__(self, size=0):
        """ instantiation of size to zero """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ calculates the area of the square """
        return (self.__size ** 2)
