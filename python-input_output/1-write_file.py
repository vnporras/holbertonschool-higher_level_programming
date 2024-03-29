#!/usr/bin/python3
"""Write file"""
def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters written"""
    with open(filename, "w") as file:
        file.write(text)
