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
        self.assertTrue(isinstance(s, Base))
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

    def test_errors_display_method(self):
        """check for errors"""
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

    def test_update_method(self):
        """check update method with *args and **kwargs arguments"""
        s = Square(3, 3)
        self.assertEqual(str(s), '[Square] (1) 3/0 - 3')
        s.update(90)
        self.assertEqual(s.id, 90)
        self.assertEqual(str(s), "[Square] (90) 3/0 - 3")
        s.update(54, 2)
        self.assertEqual(s.width, 2)
        self.assertEqual(str(s), "[Square] (54) 3/0 - 2")
        s.update(89, 2, 8)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.height, 2)
        self.assertEqual(str(s), "[Square] (89) 8/0 - 2")
        s.update(90, 2, 8, 4)
        self.assertEqual(s.x, 8)
        self.assertEqual(s.y, 4)
        self.assertEqual(str(s), "[Square] (90) 8/4 - 2")
        s.update(89, 2, 3, 4, 5, 6, 7)
        self.assertEqual(str(s), "[Square] (89) 3/4 - 2")
        s.update()
        self.assertEqual(str(s), "[Square] (89) 3/4 - 2")
        s.update(size=1)
        self.assertEqual(s.height, 1)
        s.update(size=1, x=2)
        self.assertEqual(s.width, 1)
        s.update(y=1, size=22, x=3, id=89)
        self.assertEqual(str(s), '[Square] (89) 3/1 - 22')
        s.update(x=1, y=3, size=4)
        self.assertEqual(str(s), '[Square] (89) 1/3 - 4')
        s.update(2, 5, 4, 6, size=65, x=2)
        self.assertEqual(str(s), '[Square] (2) 4/6 - 5')

    def test_errors_update_method(self):
        """check update method for errors"""
        s = Square(3, 3)
        with self.assertRaises(TypeError):
            s.update(2, "4", 6)
        with self.assertRaises(ValueError):
            s.update(2, 4, 6, -3)
        with self.assertRaises(TypeError):
            s.update(x='kite')
        with self.assertRaises(TypeError):
            s.update(x=2, size="high")
        with self.assertRaises(ValueError):
            s.update(size=65, x=-8)

    def test_to_dictionary_method(self):
        """check to_dictionary method"""
        s = Square(10, 2, 1)
        self.assertEqual(s.to_dictionary(), {'x': 2, 'y': 1,
                                             'id': 1, 'size': 10})
        self.assertCountEqual(s.to_dictionary(), {'x': 2, 'y': 1,
                                                  'id': 1, 'size': 10})
        self.assertTrue(type(s.to_dictionary()), dict)
        s2 = Square(1, 1)
        s2.update(**s.to_dictionary())
        self.assertEqual(s2.__str__(), '[Square] (1) 2/1 - 10')
        self.assertFalse(s == s2)
        with self.assertRaises(TypeError):
            s.to_dictionary(4)


if __name__ == '__main__':
    unittest.main()
