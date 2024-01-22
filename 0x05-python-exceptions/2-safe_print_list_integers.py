#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    integer_count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]))
                integer_count += 1
    except IndexError:
        pass
    finally:
        return integer_count
