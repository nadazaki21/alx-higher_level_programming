#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print(
            "Inside result: {:.1f}".format(
                result) if result is not None else "Inside result: None")
    return result
