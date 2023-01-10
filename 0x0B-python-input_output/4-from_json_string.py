#!/usr/bin/python3
"""
Module imported
"""
import json


def from_json_string(my_str):
    """
    a method that takes a string and convert it to
    a JSON formatted
    """
    return json.loads(my_str)
