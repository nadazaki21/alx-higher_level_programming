#!/usr/bin/python3
""" My List class """


class MyList(list):
    """ class MyList that inherits from list """
    def print_sorted(self):
        print(sorted(self))
