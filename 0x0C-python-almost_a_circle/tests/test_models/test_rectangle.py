#!/usr/bin/python3
"""
rectangle class unittest
"""

from models.base import Base
from models.rectangle import Rectangle
import unittest
import contextlib
from io import StringIO


class TestRectangleClass(unittest.TestCase):
    """various tests"""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_attrs(self):
        """check rect obj attributes; id, width, height x and y"""
        r1 = Rectangle(5, 7)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.height, 7)
        self.assertEqual(r1.width, 5)
        r2 = Rectangle(4, 10)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r3 = Rectangle(5, 2, 3, 4, 12)
        self.assertEqual(r3.id, 12)

    def test_missing_args(self):
        """check for missing arguments"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(2)
        with self.assertRaises(TypeError):
            r2 = Rectangle()

    def test_classtype(self):
        """check for class type and subclasses"""
        r = Rectangle(3, 2)
        self.assertTrue(isinstance(r, Rectangle))
        self.assertTrue(issubclass(type(r), Base))

    def test_err_attr(self):
        """check for error ; wrong arguments types and value"""
        with self.assertRaises(TypeError):
            a = Rectangle("with", 3)
        with self.assertRaises(ValueError):
            b = Rectangle(4, -2)
        with self.assertRaises(ValueError):
            c = Rectangle(4, 3, -2, 1)
        with self.assertRaises(TypeError):
            d = Rectangle(4, True)
        with self.assertRaises(TypeError):
            e = Rectangle((0,), 4)
        with self.assertRaises(TypeError):
            a = Rectangle(4, 3, 2, "4")
        with self.assertRaises(TypeError):
            a = Rectangle(4, 3, "2", 4)
        with self.assertRaises(TypeError):
            c = Rectangle(4, 3, 0, 1.8)
        with self.assertRaises(ValueError):
            e = Rectangle(10, 0)
        with self.assertRaises(TypeError):
            a = Rectangle(None, 3)
        with self.assertRaises(TypeError):
            a = Rectangle(14, [3, 3])
        with self.assertRaises(TypeError):
            a = Rectangle(14, {3, 3}, 3, 4)

    def test_area_method(self):
        """check for correct area value"""
        r = Rectangle(3, 7)
        self.assertEqual(r.area(), 21)
        r1 = Rectangle(320, 452)
        self.assertEqual(r1.area(), 144640)

    def test_display_method(self):
        """check rect display"""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r = Rectangle(3, 3)
            r.display()
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, '###\n###\n###')

        temp_stdout2 = StringIO()
        with contextlib.redirect_stdout(temp_stdout2):
            r1 = Rectangle(3, 2, 2, 1)
            r1.display()
        output2 = temp_stdout2.getvalue()
        self.assertEqual(output2, "\n  ###\n  ###\n")

        with self.assertRaises(TypeError) as x:
            r1 = Rectangle(9, 6)
            r1.display(9)

    def test_str_method(self):
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r = Rectangle(5, 2, 7, 3)
            print(r)
        output = temp_stdout.getvalue().strip()
        assert output == '[Rectangle] (1) 7/3 - 5/2'

    def test_update_args_method(self):
        """test update method with *args and *kwargs"""
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")

        r1.update(90)
        self.assertEqual(r1.id, 90)
        self.assertEqual(r1.__str__(), "[Rectangle] (90) 10/10 - 10/10")

        r1.update(54, 2)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (54) 10/10 - 2/10")

        r1.update(89, 2, 8)
        self.assertEqual(r1.height, 8)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/8")

        r1.update(90, 2, 8, 4)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (90) 4/10 - 2/8")

        r1.update(89, 2, 3, 4, 5, 6, 7)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

        r1.update()
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")



if __name__ == '__main__':
    unittest.main()
