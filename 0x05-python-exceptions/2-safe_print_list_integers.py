#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    integer_count = 0
    try:
        for i in my_list[0:x]:
            print("{:d}".format(i), end="\n" if isinstance(i, int) else "")
            integer_count += isinstance(i, int)
    except IndexError:
        print("list index out of range")
    finally:
        return integer_count