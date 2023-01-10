#!/usr/bin/python3
"""
module imported
"""
import json


def load_from_json_file(filename):
    """
    a method that creates an object from json
    """
    with open(filename) as f:
        return json.load(f)
