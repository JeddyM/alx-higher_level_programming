#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    '''A function that deletes the item at a specific position in a list.'''
    if idx > (len(my_list) - 1) or idx < 0:
        return my_list
    else:
        del my_list[idx]
        return my_list
