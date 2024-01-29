#!/usr/bin/python3
"""
class Rectangle that defines a rectangle

This module provides a simple Rectangle class with attribute width and height.
Default values of both attributes are 0.
"""


class Rectangle:
    """ defines a rectangle with a width and a height """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

    def __str__(self):
        rec = ""
        if self.width == 0 or self.height == 0:
            return rec
        else:
            for h in range(self.height):
                for w in range(self.width):
                    rec += str(self.print_symbol)
                if h != self.height - 1:
                    rec += "\n"
        return rec

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def eval(self):
        obj = repr(self)
        return obj

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
