#!/usr/bin/python3

def print_square(size):
    if type(size) is not int:
        """Raise an error if size is not an integer"""
        raise TypeError("size must be an integer")
    
    if size < 0:
        """Raise an error if size is less than 0"""
        raise ValueError("size must be >= 0")
    
    if type(size) is float and size < 0:
        """Raise an error if size is a negative float"""
        raise TypeError("size must be an integer")
    
    for i in range(size):
        print("#" * size)
