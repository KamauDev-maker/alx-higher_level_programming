#!/usr/bin/python3
"""
Modules imported
"""
import json


def to_json_string(my_obj):
    """
    method that takes an object and converts it to
    a JSON formatted string
    """
    return json.dumps(my_obj)
