#!/usr/bin/python3
"""
A function that hat prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of
    these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_char_flag = 0
    for i in text:
        if i == '.' or i == '?' or i == ':':
            print("{}\n\n".format(i), end="")
            special_char_flag = 1
        else:
            if special_char_flag == 1:
                special_char_flag = 0
                pass
            else:
                print(i, end="")
