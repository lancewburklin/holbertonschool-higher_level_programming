"""
Main Test file for finding the max integer
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class testMax(unittest.TestCase):
    """Test Class"""

    def test_max(self):
        """First test for max_int"""
        list_1 = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(max_integer(list_1), 5)
