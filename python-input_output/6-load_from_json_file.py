#!/usr/bin/python3
import json

"""Load from JSON file"""


def load_from_json_file(filename):
    """creates an Object from a "JSON file"""
    with open(filename, "r") as f:
        return json.load(f)
