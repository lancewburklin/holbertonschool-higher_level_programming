#!/usr/bin/python3
"""
Square tests
"""
from models.square import Square
import unittest


class TestSquare(unittest.TestCase):
    """Test cases"""

    def test_10(self):
        """test for problem 10"""
        s1 = Square(10, id=7)
        self.assertEqual(str(s1), "[Square] (7) 0/0 - 10")
        self.assertAlmostEqual(s1.area(), 100)
        s1.update(31, x=3, y=7)
        self.assertEqual(str(s1), "[Square] (31) 3/7 - 10")
