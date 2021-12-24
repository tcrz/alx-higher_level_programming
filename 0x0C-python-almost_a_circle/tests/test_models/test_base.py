#!/usr/bin/python3
"""
Unittest for base Class
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    def setUp(self):
        """create Base objects"""
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()

    def test_baseclass_attr(self):
        """check obj attributes"""
        self.assertEqual(self.b1.id, 1)
        self.b1.id = 32
        self.assertEqual(self.b1.id, 32)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)

    def tearDown(self):
        """delete base objects"""
        del self.b1
        del self.b2


if __name__ == '__main__':
    unittest.main()
