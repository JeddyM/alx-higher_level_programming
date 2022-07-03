#!/usr/bin/python3
def element_at(my_list, idx):
    '''Function that replaces an element of a list'''
    if idx < 0:
        return None
    elif idx > (len(my_list) - 1):
        return None
    else:
        return my_list[idx]
