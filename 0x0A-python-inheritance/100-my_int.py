#!/usr/bin/python3
"""
Creates a new class
"""


class MyInt(int):
    """Just reverses == and !="""

    def __eq__(self, other):
        """Equal to"""
        return int(self) != other

    def __ne__(self, other):
        """"Not Equal to"""
        return int(self) == other
