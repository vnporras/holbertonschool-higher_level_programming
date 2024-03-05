#!/usr/bin/python3

def add_integer(a, b=98):
    """Add two integers"""
    types = [int, float]
    
    if type(a) not in types:
        """Raise an error if a is not an integer or float"""
        raise TypeError("a must be an integer")

    if type(b) not in types:
        """Raise an error if b is not an integer or float"""
        raise TypeError("b must be an integer")
    
    if type(a) is float:
        """Convert a to an integer if it is a float"""
        a = int(a)

    if type(b) is float:
        """Convert b to an integer if it is a float"""
        b = int(b)

    return a + b
