#!/usr/bin/python3
""" Defines a class of "Square" and its attributes """


class Square:
    """ defines a square

    Args:
        size: size of the square

    Return:
        The area of the square
    """
    def __init__(self, size=0):
        """ instantiation of size equal to zero """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    # getting the values
    @property
    def size(self):
        """ get the new value of the size """
        return self.__size

    # setting the values
    @size.setter
    def size(self, value):
        """ set the new value of size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns the area of the size """
        return self.__size ** 2

    def my_print(self):
        """ prints out the area of the square with the character # """
        for i in range(self.__size):
            print("#"*self.__size)
        if self.__size == 0:
            print("#"*0)
