#!/usr/bin/python3

def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8) and returns the number of characters written"""
    with open(filename, "a") as f:
        return f.write(text)
