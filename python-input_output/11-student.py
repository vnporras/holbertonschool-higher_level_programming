#!/usr/bin/python3
"""Module to create a class Student"""


class Student:
    """Class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Constructor of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is not None and type(attrs) is list:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Method that replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
