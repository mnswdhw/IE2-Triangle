import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class TestStatementCoverage(unittest.TestCase):

    def test1(self):
        # Test case to cover statement 1
        actual = Triangle.classify(10, 10, 10)
        expected=Triangle.Type.EQUILATERAL
        self.assertTrue(actual,expected)

    def test2(self):
        actual = Triangle.classify(10, -10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test3(self):
        actual = Triangle.classify(3, 4, 5)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)
    def test4(self):
        actual = Triangle.classify(3, 4, 8)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test5(self):
        actual = Triangle.classify(10, 10, 15)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    
    # Add more test cases for other statements

if __name__ == '__main__':
    unittest.main()





