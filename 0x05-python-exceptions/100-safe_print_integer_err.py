#!/usr/bin/python3
def safe_print_integer_err(value):
    result = None
    try:
        print("{:d}".format(value))
        result = True
    except (TypeError, ValueError):
        result = False
    finally:
        return result
