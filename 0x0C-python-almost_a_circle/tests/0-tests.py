#!/usr/bin/python3
"""Unittest for problem 0"""


import unittest
from models.base import Base
class Test_Base(unittest.TestCase):
    """Beginning of the test class"""

    def test_one(self):
        """First set of tests"""
        b1 = Base()
        self.assertAlmostEqual(b1.id, 1)
        b2 = Base()
        self.assertAlmostEqual(b2.id, 2)
        b3 = Base()
        self.assertAlmostEqual(b3.id, 3)
        b4 = Base(12)
        self.assertAlmostEqual(b4.id, 12)
        b5 = Base()
        self.assertAlmostEqual(b5.id, 4)

    def test_two(self):
        """Second set of tests"""
        b1 = Base(100)
        self.assertAlmostEqual(b1.id, 100)
