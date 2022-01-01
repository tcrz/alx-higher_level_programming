#!/usr/bin/python3
"""
Unittest for base Class
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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
        self.assertIsInstance(b4, Base)

    def test_to_json_string(self):
        """test to_json_string static method"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(
            json_dictionary,
            '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]')
        self.assertCountEqual(
            json_dictionary,
            '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]')
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, '[]')
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, '[]')

    def test_err_to_json_string(self):
        """test for errors with wrong arguments"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        with self.assertRaises(TypeError):
            json_dictionary = Base.to_json_string([dictionary, 5])
        with self.assertRaises(TypeError):
            json_dictionary = Base.to_json_string("Jhan")
        with self.assertRaises(TypeError):
            json_dictionary = Base.to_json_string()
        with self.assertRaises(TypeError):
            json_dictionary = Base.to_json_string("Jhan", [{'k': 8}])
        with self.assertRaises(TypeError):
            json_dictionary = Base.to_json_string(dictionary)
        with self.assertRaises(TypeError):
            json_dictionary = Base.to_json_string(True)
        with self.assertRaises(TypeError):
            json_dictionary = Base.to_json_string(5)
        with self.assertRaises(TypeError):
            json_dictionary = Base.to_json_string(5.3)
        with self.assertRaises(TypeError):
            json_dictionary = Base.to_json_string([8, 5])
        with self.assertRaises(TypeError):
            json_dictionary = Base.to_json_string((8, 5))
        with self.assertRaises(TypeError):
            json_dictionary = Base.to_json_string({'k': 8})

    def test_save_to_file(self):
        """test save_to_file class method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r", encoding='utf-8') as file:
            stream = file.read()
        self.assertEqual(
            stream, '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, \
{"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]')
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r", encoding='utf-8') as file:
            stream = file.read()
        self.assertEqual(stream, '[]')
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding='utf-8') as file:
            stream = file.read()
        self.assertEqual(stream, '[]')
        s1 = Square(4, 7, 3)
        s2 = Square(2, 4, 9, 6)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r", encoding='utf-8') as file:
            stream = file.read()
        self.assertCountEqual(
            stream, '[{"id": 3, "size": 4, "x": 7, "y": 3}, \
{"id": 6, "size": 2, "x": 4, "y": 9}]'
        )
        Square.save_to_file([])
        with open("Square.json", "r", encoding='utf-8') as file:
            stream = file.read()
        self.assertEqual(stream, '[]')
        Square.save_to_file(None)
        with open("Square.json", "r", encoding='utf-8') as file:
            stream = file.read()
        self.assertEqual(stream, '[]')

    def test_err_save_to_file(self):
        """test for errors and wrong args in save_to_file class method"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(3, 4)
        with self.assertRaises(AttributeError):
            Square.save_to_file([3, 4])
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(3)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_from_json_string(self):
        """test from_json_method"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertIsInstance(list_ouput, str)
        self.assertCountEqual(list_output,
                              Rectangle.from_json_string(json_list_input))
        self.assertEqual(list_output,
                         Rectangle.from_json_string(json_list_input))
        json_list_input = Rectangle.to_json_string('')
        self.assertCountEqual(list_output, [])
        json_list_input = Rectangle.to_json_string('None')
        self.assertCountEqual(list_output, [])

    def test_from_json_string(self):
        """test errors and wrong arguments on from_json_method"""
        with self.assertRaises(TypeError):
            Square.from_json_string(4, 4)
        with self.assertRaises(TypeError):
            Square.from_json_string(4)
        with self.assertRaises(TypeError):
            Square.from_json_string({'id': '3'})
        with self.assertRaises(TypeError):
            Square.from_json_string([3, 3])

    def test_create(self):
        """test create method"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsInstance(r2, Rectangle)
        self.assertEqual(str(r2), '[Rectangle] (1) 1/0 - 3/5')
        self.assertEqual(str(r2), str(r1))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)
        r1 = Square(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertIsInstance(r2, Square)
        self.assertEqual(str(r2), '[Square] (3) 5/1 - 3')
        self.assertEqual(str(r2), str(r1))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_err_create(self):
        """test errors and wrong arguments on create method"""
        with self.assertRaises(TypeError):
            Rectangle.create(4)

    def test_load_from_file(self):
        """Test class method load_from_file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))
        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4)
        list_square_input = [r1, r2]
        Square.save_to_file(list_square_input)
        list_rectangles_output = Square.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file(self):
        """test with wrong args"""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output, [])
        list_squares_output = Square.load_from_file()
        self.assertEqual(list_squares_output, [])

    def test_load_from_file_csv(self):
        "test"
        r0 = Rectangle(7, 3, 2, 5)
        r1 = Rectangle(5, 4)
        Rectangle.save_to_file_csv([r0, r1])
        with open("Rectangle.csv", "r") as file:
            stream = file.read()
            self.assertEqual(stream, "7,3,2,5,1\n5,4,0,0,2\n")
            self.assertCountEqual(stream, "7,3,2,5,1\n5,4,0,0,2\n")
        s0 = Square(9, 3, 1, 12)
        s1 = Square(6, 7)
        Square.save_to_file_csv([s0, s1])
        res = "9,3,1,12\n6,7,0,3\n"
        with open("Square.csv", "r") as file:
            stream = file.read()
            self.assertEqual(stream, "9,3,1,12\n6,7,0,3\n")
            self.assertCountEqual(stream, "9,3,1,12\n6,7,0,3\n")


if __name__ == '__main__':
    unittest.main()
