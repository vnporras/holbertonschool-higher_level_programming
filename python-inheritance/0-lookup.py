#!/usr/bin/python3

def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)

"""Empty class MyClass1."""
class MyClass1(object):
    """Empty class MyClass1."""
    pass

"""class MyClass2 with attributes and methods"""
class MyClass2(object):
    """class MyClass2 with attributes and methods."""
    my_attr1 = 3
    def my_meth(self):
        """Return the value of my_attr1."""
        pass
