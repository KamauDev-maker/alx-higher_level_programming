#!/usr/bin/python3
"""
Module imported
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A method that defines the object and the filename
    and write the JSON representation
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
