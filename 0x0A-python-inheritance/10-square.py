#!/usr/bin/python3
"""
module containing a class Square that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """return a string representation of the square"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

    def area(self):
        """return the area of the square"""
        return self.__size ** 2
