"""
Main Test file for finding the max integer
"""


import unittest
import math
max_integer = __import__('6-max_integer').max_integer


class testMax(unittest.TestCase):
    """Test Class"""

    def test_max(self):
        """First test for max_int"""
        list_1 = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(max_integer(list_1), 5)
        list_1.append(7)
        self.assertAlmostEqual(max_integer(list_1), 7)

    def test_two(self):
        """Second test for max_int"""
        list_2 = [2, 4, 6, 8, 8.5, 3, 2]
        self.assertAlmostEqual(max_integer(list_2), 8.5)

    def test_three(self):
        """Third test for max_int"""
        list_3 = [-2, -3, -4, -5, -6]
        self.assertAlmostEqual(max_integer(list_3), -2)

    def test_four(self):
        """Fourth test for max_int"""
        list_4 = []
        self.assertAlmostEqual(max_integer(list_4), None)

    def test_five(self):
        """Fith test for max_int"""
        list_5 = [(5 - 5), -1, -2, -3, -4]
        self.assertAlmostEqual(max_integer(list_5), 0)

    def test_six(self):
        """Sixth test for max_int"""
        list_6 = [9000, -500, -1000]
        self.assertAlmostEqual(max_integer(list_6), 9000)

    def test_seven(self):
        """Seventh test for max_int"""
        list_7 = [1, 2, 3]
        list_71 = [4, 5, 6]
        self.assertAlmostEqual(max_integer(list_7 + list_71), 6)

    def test_eight(self):
        """Eigth test for max_int"""
        list_8 = [13, 12, -5, -6, 7]
        self.assertAlmostEqual(max_integer(list_8), 13)

    def test_nine(self):
        """Ninth test for max_int"""
        list_9 = [(100 ** 2), 3, 5, -6]
        self.assertAlmostEqual(max_integer(list_9), 10000)

    def test_ten(self):
        """Tenth test for max_int"""
        list_10 = [math.sqrt(100), 1, 2, 3, 4]
        self.assertAlmostEqual(max_integer(list_10), 10)

    def test_eleven(self):
        """Eleventh test for max_int"""
        list_11 = [1]
        self.assertAlmostEqual(max_integer(list_11), 1)

    def test_twelve(self):
        """Test twelve for max_int"""
        list_12 = [1, 1]
        self.assertAlmostEqual(max_integer(list_12), 1)

    def test_thirteen(self):
        """Test number thirteen"""
        list_13 = ["test", "testit", "testitCheese"]
        self.assertEqual(max_integer(list_13), "testitCheese")

    def test_fourteen(self):
        """Test number fourteen"""
        list_14 = "TEST"
        self.assertEqual(max_integer(list_14), 'T')

    def test_15(self):
        """Test number 15"""
        b = float("inf")
        list_15 = [2, 4, 6, b]
        self.assertEqual(max_integer(list_15), b)

    def test_16(self):
        """Test number 16"""
        b = float("nan")
        list_16 = [2, 4, 6, b]
        self.assertAlmostEqual(max_integer(list_16), 6)
