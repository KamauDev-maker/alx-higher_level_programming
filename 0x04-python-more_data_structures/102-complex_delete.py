#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = []
    for k, v in a_dictionary.items():
        if v is value:
            new_dict.append(k)
    for x in new_dict:
        del a_dictionary[x]
    return(a_dictionary)
