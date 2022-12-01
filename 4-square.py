#!/usr/bin/python3
""" Defines a class "Square" and its attributes """


class Square:
    """ defines a square that must be of integer data type

        Args:
            size: size of the square

        Return:
            Nothing
    """
    def __init__(self, size=0):
        """ Instantiate the square with size equals zero """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    # getting the size
    @property
    def size(self):
        """ retrieves the new value from the setter """
        return self.__size

    # setting the size
    @size.setter
    def size(self, value):
        """ sets the value of the private instance attribute
            Args:
                value: new size value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ public instance method that gives area of the square"""
        return self.__size ** 2
