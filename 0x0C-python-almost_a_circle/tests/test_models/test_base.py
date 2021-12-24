#!/usr/bin/python3
"""
Unittest for base Class
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    def setUp(self):
      Base._Base__nb_objects = 0


    def test_baseclass_attr(self):
        """check obj attributes"""
        b1 = Base()
        b2 = Base()
        b3 = Base(None)
        self.assertEqual(b1.id, 1)
        b1.id = 32
        self.assertEqual(b1.id, 32)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_classtype(self):
        b4 = Base()
        self.assertTrue(isinstance(b4, Base))


if __name__ == '__main__':
    unittest.main()
