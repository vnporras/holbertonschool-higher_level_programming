#!/usr/bin/python3
def no_c(my_string):
    char_list = list(my_string)
    new_list = [char for char in char_list if char not in ('c', 'C')]
    result = ''.join(new_list)
    return result
