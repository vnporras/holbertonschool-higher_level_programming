#!/usr/bin/python3
"""Return True if obj is an instance of a class that inherited from cls."""


def inherits_from(obj, a_class):
    """Check if the object is an instance of a class that inherited from the specified class"""
    if type(obj) is a_class:
        return False

    return issubclass(type(obj), a_class)
