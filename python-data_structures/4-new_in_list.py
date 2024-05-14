#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        cp_list = my_list[:]
        cp_list[idx] = element
        return cp_list
    else:
        return my_list
