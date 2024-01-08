#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """the custom MyList class"""
    def print_sorted(self):
        """the method for printing sorted list"""
        print(sorted(self))
