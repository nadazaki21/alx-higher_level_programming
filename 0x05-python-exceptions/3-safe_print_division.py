#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        flag = 0
        result = a / b
        flag = 1
    except ZeroDivisionError:
        print(" can not divide by zero")
    finally:
        print(
            "Inside result: {:1f}".format(
                result) if flag else "Inside result: None")
