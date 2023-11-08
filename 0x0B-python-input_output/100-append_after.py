#!/usr/bin/python3
"""
Module for appending a line of text after each occurrence
of a specific string in a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line
    containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The specific string to
        search for in each line.
        new_string (str): The line of text to insert
        after each occurrence of search_string.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, mode='w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)


append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
