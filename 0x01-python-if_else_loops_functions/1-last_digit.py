#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Determine the sign and calculate the last digit

if number < 0:
    sign = -1
else:
    sign = 1

last_digit = abs(number) % 10 * sign

if (last_digit < 6) and (last_digit != 0):
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, last_digit))
elif last_digit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, last_digit))
else:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, last_digit))
