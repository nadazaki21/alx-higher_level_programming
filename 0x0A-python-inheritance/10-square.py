#!/usr/bin/python3
"""
===================================
module with class BaseGeometry
===================================
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

    def area(self):
        """ calculates area """
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height)


class Square(Rectangle):
    """Square class that inherits from Rectangle that inherits BaseGeometry"""

    def __init__(self, size):
        """Method for initialized the attrubutes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """rectangle area"""

        return self.__size ** 2
