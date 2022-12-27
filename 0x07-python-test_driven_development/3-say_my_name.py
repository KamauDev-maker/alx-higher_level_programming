#!/usr/bin/python3
"""
No module imported
"""


def say_my_name(first_name, last_name=""):
    """
    method that defines the property object summary

    first_name: should be a string
    last_name: should be a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
