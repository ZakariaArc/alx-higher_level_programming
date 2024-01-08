#!/usr/bin/python3
""""
Contains a function that appends a string
at the end of a text file (UTF8)
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8)
    and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)


if __name__ == "__main__":
    filename = "file_append.txt"
    text = "This School is so cool!\n"
    nb_characters_added = append_write(filename, text)
    print(nb_characters_added)
