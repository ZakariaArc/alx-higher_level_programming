#!/usr/bin/python3
"""
module containing a class MyList that inherits from list.
"""


class MyList(list):
    """inherits from list and provides additional functionality."""

    def print_sorted(self):
        """prints the list in ascending order."""
        print(sorted(self))
