#!/usr/bin/python3
"""
This is a class for sorting things
"""


class MyList(list):
    """This class MyList"""

    def print_sorted(self):
        """The sort method"""
        new_sort = self.copy()
        new_sort.sort()
        print("{}".format(new_sort))
