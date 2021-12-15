#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        """tests with max_integer func. should return max integer"""
        self.assertEqual(max_integer([50, 30, 54]), 54)
        self.assertEqual(max_integer([50.32, -30, -54]), 50.32)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([123, 432, 100]), 432)
        self.assertEqual(max_integer([-23, -34,-200]), -23)
        self.assertEqual(max_integer([130]), 130)

    def test_errors(self):
        """tests with max_integer func. should raise TypeError exception"""
        self.assertRaises(TypeError, max_integer, 4)
        self.assertRaises(TypeError, max_integer, 5.5)
        self.assertRaises(TypeError, max_integer, [2, 3.4, "str"])


if __name__ == "__main__":
    unittest.main()
