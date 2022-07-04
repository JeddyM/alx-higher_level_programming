#/usr/bin/env python3
def no_c(my_string):
    '''A function that removes all characters c and C from a string.'''
    new_string = my_string.translate({ord(i): None for i in 'Cc'})
    return new_string
