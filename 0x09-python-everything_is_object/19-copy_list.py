#!/usr/bin/python3
"""
This script contains a function 'copy_list' that returns a copy of a list.
The input list can contain any type of objects.
The function uses list slicing to create a new
list with the same elements as the original list.
"""


def copy_list(input_list):
    """
    Returns a copy of the input list.

    :param input_list: The input list to be copied.
    :return: A new list with the same elements as the original list.
    """
    return input_list[:]
