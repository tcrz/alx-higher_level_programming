#!/usr/bin/python3
"""
Test for Square class
"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import contextlib
from io import StringIO


class TestSquareClass(unittest.TestCase):
    """various tests"""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_classtype(self):
        """check for Square obj type and subclasses"""
        s = Square(3)
        self.assertTrue(type(s), Square)
        self.assertTrue(isinstance(s, Rectangle))
        self.assertTrue(issubclass(type(s), Rectangle))
        self.assertTrue(issubclass(type(s), Base))

    def test_attrs(self):
        """check Square obj attributes; id, width, height x and y"""
        s = Square(3, 4)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.height, 3)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 0)

    def test_missing_args(self):
        """check for missing arguments"""
        with self.assertRaises(TypeError):
            s = Square()

    def test_wrong_attrs(self):
        """check for error ; wrong arguments types and value"""
        with self.assertRaises(TypeError):
            s = Square(8, "9")
        with self.assertRaises(ValueError):
            s = Square(3, 3, -4, 2)
        with self.assertRaises(TypeError):
            s = Square("Jam")
        with self.assertRaises(ValueError):
            s = Square(0)
        with self.assertRaises(TypeError):
            s = Square(None)
        with self.assertRaises(TypeError):
            s = Square(3, [2], 3, 5)
        with self.assertRaises(TypeError):
            s = Square(8, False)
        with self.assertRaises(TypeError):
            s = Square(3, 3, (3, 3), 5)
        with self.assertRaises(TypeError):
            s = Square({3, 3}, 3, 5)
        with self.assertRaises(TypeError):
            s = Square(3, 3, 2.4, 2)

    def test_area_method(self):
        """check area method returns correct value"""
        s = Square(41)
        self.assertEqual(s.area(), 1681)

    def test_display_method(self):
        """check display method"""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r = Square(3, 3)
            r.display()
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, '###\n   ###\n   ###')

        temp_stdout2 = StringIO()
        with contextlib.redirect_stdout(temp_stdout2):
            r1 = Square(3, 2, 1)
            r1.display()
        output2 = temp_stdout2.getvalue()
        self.assertEqual(output2, '\n  ###\n  ###\n  ###\n')

        with self.assertRaises(TypeError) as x:
            r1 = Square(9, 6)
            r1.display(9)

    def test_str_method(self):
        """check output for str method"""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r = Square(3, 3, 1, 20)
            print(r)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, '[Square] (20) 3/1 - 3')


if __name__ == '__main__':
    unittest.main()
