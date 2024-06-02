#!/usr/bin/python3
"""Write file"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8)"""
    with open(filename, "w") as file:
        file.write(text)
