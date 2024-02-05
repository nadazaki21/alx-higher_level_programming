#!/usr/bin/python3
"""
========================================
BaseGGeomtry and Rectangle class
========================================
"""


class BaseGeometry():
    """ class callled base geomety"""
    def area(self):
        """ function  that calculates the area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method for validating the value entered """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ class that represnts a rectangle """
    def __init__(self, width, height):
        """ method to intialize the widht nad height of a rectangle """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
