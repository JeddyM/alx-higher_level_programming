#!/usr/bin/python3
def best_score(a_dictionary):
    '''A function that returns a key with the biggest integer value.'''
    if not isinstance(a_dictionary, dict) not len(a_dictionary) == 0:
        return None
    my_list = list(a_dictionary.keys())[0]
    big_int = a_dictionary[my_list]
    for n, i in a_dictionary.items():
        if i > big_int:
            big_int = i
            my_list = n
    return my_list
