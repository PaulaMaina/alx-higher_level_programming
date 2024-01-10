#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_keys =  sorted(a_dictionary)
    dict_new = {}
    for k in dict_keys:
        dict_new[k] = a_dictionary[k]
    for k in dict_new:
        print("{}: {}".format(k, dict_new[k]))
