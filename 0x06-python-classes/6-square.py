#!/usr/bin/python3
""" Square class """


class Square():
    """ class that defines a square """

    def __init__(self, size=0, position=(0, 0)):
        if (isinstance(size, int) != 1):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if (
            not isinstance(position, tuple) or len(position) != 2 or not all(
                (isinstance(i, int) and i >= 0 for i in position))):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        return (self.__size*self.__size)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if (isinstance(value, int) != 1):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple) or len(value) != 2 or not all(
                (isinstance(i, int) and i >= 0 for i in value))):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            [print("\n", end="") for n in range(self.__position[1])]
            for i in range(self.__size):
                [print(" ", end="") for m in range(self.__position[0])]
                for j in range(self.__size):
                    print("#", end="")
                print()
