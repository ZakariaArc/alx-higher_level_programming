#!/usr/bin/python3
"""
Module that contains the MyList class
"""


class MyList(list):
    """A subclass of the list"""
    def __init__(self):
        """Initializes the object"""
        super().__init__()

    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
