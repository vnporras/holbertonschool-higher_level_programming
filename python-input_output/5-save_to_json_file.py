#!/usr/bin/python3
import json

"""Save to JSON file"""


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, "w") as f:
        return f.write(json.dumps(my_obj))