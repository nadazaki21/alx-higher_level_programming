#!/usr/bin/python3
""" Square class """


class Square():
    """ class that defines a square """

    def __init__(self, size=0):
        if (isinstance(size, int) != 1):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

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

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                print()
