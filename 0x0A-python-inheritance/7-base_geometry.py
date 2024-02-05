#!/usr/bin/python3
""" Base gepomtry class  """


class BaseGeometry():
    """ class callled base geomety"""
    def area(self):
        """ method to calculate area , not implemented for now """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method to validate entered inetegr values """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
