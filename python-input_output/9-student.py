#!/usr/bin/python3
"""Module to create a class Student"""


class Student:
    """Class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Constructor of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
