#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 and idx >= len(my_list):
        return my_list

    result = my_list.copy()
    counter = 0
    my_list.clear()

    while counter < len(result):
        if counter != idx:
            my_list.append(result[counter])
        counter = counter + 1

    return my_list
