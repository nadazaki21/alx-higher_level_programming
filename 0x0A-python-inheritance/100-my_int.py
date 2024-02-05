#!/usr/bin/python3
"""
MyInt class
"""


class MyInt(int):
    """ MyInt is a rebel. MyInt has == and != operators inverted """

    def __eq__(self, other):
        # Override equality operator ==
        return super().__ne__(other)  # Call inequality operator

    def __ne__(self, other):
        # Override inequality operator !=
        return super().__eq__(other)  # Call equality operator
