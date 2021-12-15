#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        """tests with max_integer func. should return max integer"""
        self.assertEqual(max_integer([50, 30, 54]), 54)
        self.assertEqual(max_integer([50, -30, -54]), 50)
        self.assertEqual(max_integer([-50, -30, -54]), -30)
        self.assertEqual(max_integer([-130, 4]), 4)

    def test_errors(self):
        """tests with max_integer func. should raise TypeError exception"""
        self.assertRaises(TypeError, max_integer, 4)
#        self.assertRaises(TypeError, max_integer, "Test")
      #  self.assertRaises(TypeError, max_integer, ["ds", "sd"])
      #  self.assertRaises(TypeError, max_integer, ["ds", []])
         self.assertRaises(TypeError, max_integer, None)


if __name__ == "__main__":
    unittest.main()
