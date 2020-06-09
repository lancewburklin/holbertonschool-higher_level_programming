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

    def test_11(self):
        """Tets 11"""
        s1 = Square(10)
        self.assertAlmostEqual(s1.size, 10)
        s1.size = 7
        self.assertAlmostEqual(s1.size, 7)
        with self.assertRaises(ValueError):
            s1.size = -10
        with self.assertRaises(TypeError):
            s1.size = {}

    def test_12(self):
        """Test 12"""
        s1 = Square(11)
        s1.update(size=3, id=19)
        self.assertAlmostEqual(s1.size, 3)
        s1.update(2, 2, 2, 2)
        self.assertEqual(str(s1), "[Square] (2) 2/2 - 2")
        s1.update(size=12)
        self.assertEqual(str(s1), "[Square] (2) 2/2 - 12")
        with self.assertRaises(ValueError):
            s1.update(size=-5)
