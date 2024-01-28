#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
# try:
print(add_integer(4, "School"))
# except Exception as e:
#     print(e)
# try:
#     print(add_integer(None))
# except Exception as e:
#     print(e)


# Traceback (most recent call last):
#   File "/home/nada-zaki/alx/alx-python/alx-higher_level_programming/0x07-python-test_driven_development/./0-main.py", line 9, in <module>
#     print(add_integer(4, "School"))
#   File "/home/nada-zaki/alx/alx-python/alx-higher_level_programming/0x07-python-test_driven_development/0-add_integer.py", line 9, in add_integer
#     raise TypeError("b must be an integer")
# TypeError: b must be an integer