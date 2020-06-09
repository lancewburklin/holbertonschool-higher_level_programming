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

    def test_6(self):
        """Tests for problem 6"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        pr1 = str(r1)
        self.assertEqual(pr1, "[Rectangle] (12) 2/1 - 4/6")

    def test_8(self):
        """Tests for problem 8"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        pr1 = str(r1)
        self.assertEqual(pr1, "[Rectangle] (10) 10/10 - 10/10")
        r1.update(7)
        pr1 = str(r1)
        self.assertEqual(pr1, "[Rectangle] (7) 10/10 - 10/10")
        r1.update(13, 13, 7, 6, 2)
        pr1 = str(r1)
        self.assertEqual(pr1, "[Rectangle] (13) 6/2 - 13/7")

    def test_9(self):
        """Test for problem 9"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(2, 2, 2, 2, 2)
        self.assertEqual(str(r1), "[Rectangle] (2) 2/2 - 2/2")
        r1.update(id=3)
        self.assertEqual(str(r1), "[Rectangle] (3) 2/2 - 2/2")
        r1.update(7, id=3)
        self.assertEqual(str(r1), "[Rectangle] (7) 2/2 - 2/2")
        r1.update(id=9, x=9, y=9, width=9, height=9)
        self.assertEqual(str(r1), "[Rectangle] (9) 9/9 - 9/9")
