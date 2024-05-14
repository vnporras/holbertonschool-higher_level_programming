#!/usr/bin/python3

def no_c(my_string):
    c_list = list(my_string)
    new_list = [char for char in c_list if char not in ('c', 'C')]
    result = ''.join(new_list)
    return result
