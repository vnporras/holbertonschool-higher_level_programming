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
        """Method that retrieves a dictionary representation of a Student instance"""
        if attrs is not None and type(attrs) is list:
            return {key: value for key, value in self.__dict__.items() if key in attrs}
