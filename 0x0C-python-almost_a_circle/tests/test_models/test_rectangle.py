#!/usr/bin/python3
"""
Test for Rectangle
"""


from models.rectangle import Rectangle
import unittest


class testRectangle(unittest.TestCase):
    """Test"""

    def test_2(self):
        """Tests from problem 2"""
        r1 = Rectangle(10, 2, 0, 0, 17)
        self.assertAlmostEqual(r1.id, 17)
        r2 = Rectangle(2, 10, 0, 0, 1800)
        self.assertAlmostEqual(r2.id, 1800)
        self.assertAlmostEqual(r2.width, 2)
        self.assertAlmostEqual(r2.height, 10)
        r3 = Rectangle(10, 2, 3, 4, 100)
        self.assertAlmostEqual(r3.x, 3)
        self.assertAlmostEqual(r3.y, 4)
        self.assertAlmostEqual(r3.id, 100)

    def test_3(self):
        """Tests for problem 3"""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.width = {}
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_4(self):
        """Tests for problem 4"""
        r1 = Rectangle(3, 2)
        self.assertAlmostEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertAlmostEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertAlmostEqual(r3.area(), 56)
