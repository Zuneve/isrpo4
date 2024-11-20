import math
import unittest
import geometric_lib

class Geometric_lib_tests(unittest.TestCase):
    def test_circle_area(self):
        self.assertEqual(geometric_lib.Circle.area(0), -1)
        self.assertEqual(geometric_lib.Circle.area(-100), -1)
        self.assertAlmostEqual(geometric_lib.Circle.area(4), 50.2654824574)
        self.assertEqual(geometric_lib.Circle.area(1), math.pi)

    def test_circle_perimeter(self):
        self.assertEqual(geometric_lib.Circle.perimeter(0), -1)
        self.assertEqual(geometric_lib.Circle.perimeter(-100), -1)
        self.assertAlmostEqual(geometric_lib.Circle.perimeter(3), 18.8495559215)
        self.assertEqual(geometric_lib.Circle.perimeter(0.5), math.pi)

    def test_rectangle_area(self):
        self.assertEqual(geometric_lib.Rectangle.area(0, 100), -1)
        self.assertEqual(geometric_lib.Rectangle.area(-100, 7), -1)
        self.assertEqual(geometric_lib.Rectangle.area(4, 9), 36)
        self.assertEqual(geometric_lib.Rectangle.area(1, 1000), 1000)

    def test_rectangle_perimeter(self):
        self.assertEqual(geometric_lib.Rectangle.perimeter(0, 100), -1)
        self.assertEqual(geometric_lib.Rectangle.perimeter(-100, 7), -1)
        self.assertEqual(geometric_lib.Rectangle.perimeter(4, 9), 26)
        self.assertEqual(geometric_lib.Rectangle.perimeter(0.5, 3), 7)

    def test_square_area(self):
        self.assertEqual(geometric_lib.Square.area(0), -1)
        self.assertEqual(geometric_lib.Square.area(-100), -1)
        self.assertEqual(geometric_lib.Square.area(4), 16)
        self.assertEqual(geometric_lib.Square.area(7), 49)

    def test_square_perimeter(self):
        self.assertEqual(geometric_lib.Square.perimeter(0), -1)
        self.assertEqual(geometric_lib.Square.perimeter(-100), -1)
        self.assertEqual(geometric_lib.Square.perimeter(5), 20)
        self.assertEqual(geometric_lib.Square.perimeter(7), 28)

    def test_triangle_area(self):
        self.assertEqual(geometric_lib.Triangle.area(7, 0), -1)
        self.assertEqual(geometric_lib.Triangle.area(9, -100), -1)
        self.assertEqual(geometric_lib.Triangle.area(4, 7), 14)
        self.assertEqual(geometric_lib.Triangle.area(3, 9), 13.5)

    def test_triangle_perimeter(self):
        self.assertEqual(geometric_lib.Triangle.perimeter(7, 5, 0), -1)
        self.assertEqual(geometric_lib.Triangle.perimeter(9, 13, -100), -1)
        self.assertEqual(geometric_lib.Triangle.perimeter(4, 7, 5), 16)
        self.assertEqual(geometric_lib.Triangle.perimeter(3, 5, 3), 11)

    def test_triangle_is_valid(self):
        self.assertFalse(geometric_lib.Triangle.is_valid(2, 5, 3))
        self.assertTrue(geometric_lib.Triangle.is_valid(3, 5, 3))
        self.assertTrue(geometric_lib.Triangle.is_valid(10, 15, 23))
        self.assertFalse(geometric_lib.Triangle.is_valid(25, 11, 13))
