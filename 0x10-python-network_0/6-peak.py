#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    """ function that finds the peak in a lsit """
    if not list_of_integers:
        return None

    number_of_elements = len(list_of_integers)
    all_equal = 1

    if number_of_elements == 1:
        return list_of_integers[0]

    if list_of_integers[0] > list_of_integers[1]:
        return list_of_integers[0]

    if (
        list_of_integers[number_of_elements - 1]
        > list_of_integers[number_of_elements - 2]
    ):
        return list_of_integers[number_of_elements - 1]

    for i in range(number_of_elements - 1):
        if list_of_integers[i] != list_of_integers[i + 1]:
            all_equal = 0

    if all_equal == 1:
        return list_of_integers[0]
    else:
        for i in range(1, number_of_elements - 1):
            if (
                list_of_integers[i] > list_of_integers[i - 1]
                and list_of_integers[i] > list_of_integers[i + 1]
            ):
                return list_of_integers[i]

        return None
