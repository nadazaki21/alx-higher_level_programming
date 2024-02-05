#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
========================================
BaseGGeomtry and Rectangle class and sqaure class
========================================
"""


class Square(Rectangle):
    """ Sqaure class that inherits Rectangle """
    def __init__(self, size):
        """ instilaizes saure size """
        super().__init__(size, size)

    def area(self):
       return super().area()