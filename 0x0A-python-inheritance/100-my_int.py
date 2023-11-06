#!/usr/bin/python3
"""
module containing a class MyInt that inherits from int.
"""


class MyInt(int):
    def __eq__(self, other):
        """inverts the == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """inverts the != operator"""
        return super().__eq__(other)
