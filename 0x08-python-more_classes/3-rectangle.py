#!/usr/bin/python3
"""
class Rectangle that defines a rectangle

This module provides a simple Rectangle class with attribute width and height.
Default values of both attributes are 0.
"""


class Rectangle:
    """ defines a rectangle with a width and a height """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)
    
    def __str__(self):
        if self.width is 0 or self.height is 0:
            print()
        else:  
            for h in range (self.height):
                for w in range(self.width):
                    print("#",end="")
                print("\n",end="")
