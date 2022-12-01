#!/usr/bin/python3
""" Defines a class of "Square" and its attributes """


class Square:
    """ defines a square

    Args:
        size: size of the square

    Return:
        The area of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ instantiation of size and position x and y to zero """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not (all([isinstance(j, int) for j in position]) and
                len(position) == 2 and all([u >= 0 for u in position])):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    # getting the size
    @property
    def size(self):
        """ get the new size """
        return self.__size

    # setting the size
    @size.setter
    def size(self, value):
        """ set the new size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    # getting the positions
    @property
    def position(self):
        """ get the new position """
        return self.__position

    # setting the position
    @position.setter
    def position(self, value):
        """ sets the new value of the position """
        if not (all([isinstance(j, int) for j in value]) and len(value) == 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ returns the area of the square """
        return self.__size ** 2

    def my_print(self):
        """ prints out the area of the square with the character # """
        [print("") for k in range(self.__position[1]) if self.__size != 0]
        for i in range(self.__size):
            [print(" "*self.__position[0], end="")]
            [print("#"*self.__size)]

        if self.__size == 0:
            print("")
