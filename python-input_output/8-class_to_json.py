#!/usr/bin/python3

"""Class to JSON"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    if hasattr(obj, "__dict__"):
        """validate if obj has __dict__ attribute, if not raise ValueError"""
        raise ValueError

    serialization_object = {}
    for key, value in obj.__dict__.items():
        """iterate over the __dict__ attribute of the object"""
        serialization_object[key] = value

    return serialization_object
