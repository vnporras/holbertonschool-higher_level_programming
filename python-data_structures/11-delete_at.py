#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 and idx >= len(my_list):
        return my_list
    
    result = []
    counter = 0

    while counter < len(my_list):
        if counter != idx:
            result.append(my_list[counter])
        counter = counter + 1
    
    return result
