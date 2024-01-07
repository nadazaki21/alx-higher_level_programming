#!/usr/bin/env python3
def no_c(my_string):
    length = len(my_string)
    i = 0
    while i < length:
        if (my_string[i] == 'c') or (my_string[i] == 'C'):
            if i == 0:
                my_string = my_string[1:]
            elif i < (length-1):
                first_half = my_string[:i]
                second_half = my_string[i+1:]
                my_string = first_half + second_half
            elif i == (length-1):
                my_string = my_string[:-1]
        i += 1
        length = len(my_string)
    return (my_string)
