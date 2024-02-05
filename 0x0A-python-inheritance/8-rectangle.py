#!/usr/bin/python3
""" 
========================================
BaseGGeomtry and Rectangle class 
========================================
"""


class BaseGeometry():
    """ class callled base geomety"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    """ class that represnts a rectangle """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
