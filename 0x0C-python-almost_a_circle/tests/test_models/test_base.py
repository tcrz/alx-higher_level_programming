#!/usr/bin/python3
"""
Unittest for base Class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


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
        """check class type"""
        b4 = Base()
        self.assertTrue(isinstance(b4, Base))

    def test_to_json_string(self):
        """test to_json_string static method"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(json_dictionary, [{"x": 2, "width": 10, "id": 1,
                                           "height": 7, "y": 8}])
        json_dictionary = Base.to_json_string([])
        self.assertTrue(json_dictionary, [])
        json_dictionary = Base.to_json_string(None)
        self.assertTrue(json_dictionary, [])

    def test_err_to_json_method(self):
        """test for errors"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        with self.assertRaises(TypeError):
            json_dictionary = Base.to_json_string([dictionary, 5])
        with self.assertRaises(TypeError):
            json_dictionary = Base.to_json_string("Jhan")
        with self.assertRaises(TypeError):
            json_dictionary = Base.to_json_string()


if __name__ == '__main__':
    unittest.main()
