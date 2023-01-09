#!/usr/bin/python3
"""
===========================
Module with class MyList
===========================
"""


class MyList(list):
    """Class with method print_sorted"""
    def print_sorted(self):
        """
        Create a copy of the list and sort it in ascending order
        """
        sorted_list = self.copy()
        sorted_list.sort()

        print(sorted_list)
