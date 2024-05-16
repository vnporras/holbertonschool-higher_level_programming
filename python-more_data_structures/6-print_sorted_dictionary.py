#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary)

    for k in keys:
        print('{}: {}'.format(k, a_dictionary[k]))

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)