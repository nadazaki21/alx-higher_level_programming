#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        largest = my_list[0]
        for i in my_list:
            if largest < i:
                largest = i
        return (largest)
