#!/usr/bin/python3
""" Class Student """


class Student():
    """ class that represents a student """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            if attrs.count != 0:
                for i in attrs:
                    if type(i) is not str:
                        return vars(self)
                valid_att = {}
                for attr_name, attr_value in self.__dict__.items():
                    for i in attrs:
                        if i == attr_name:
                            valid_att[attr_name] = attr_value
                return valid_att
            else:
                return vars(self)
        else:
            return vars(self)

