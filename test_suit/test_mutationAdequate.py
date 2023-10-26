import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class TestMutationCoverage(unittest.TestCase):

    def test1(self):
        # Test case to cover statement 1
        actual = Triangle.classify(10, 10, 10)
        expected=Triangle.Type.EQUILATERAL
        self.assertTrue(actual,expected)

    def test2(self):


        self.assertEqual(Triangle.classify(13, 6, 6), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(-12, -6, 6), Triangle.Type.INVALID)

        actual = Triangle.classify(10, -10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        actual = Triangle.classify(0, 0, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        actual = Triangle.classify(3, 4, 8)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        actual = Triangle.classify(19, -10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        actual = Triangle.classify(3, 4, -5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        actual = Triangle.classify(6, 12, 6)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        actual = Triangle.classify(12, 6, 6)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    
        actual = Triangle.classify(1, 2, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        actual = Triangle.classify(1, 3, 2)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        actual = Triangle.classify(3, 2, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        
        
        
        
    def test3(self):
        actual = Triangle.classify(3, 4, 5)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)
        self.assertEqual(Triangle.classify(3, 5, 4), Triangle.Type.SCALENE) 
        self.assertEqual(Triangle.classify(4, 3, 5), Triangle.Type.SCALENE)  

    def test5(self):
        actual = Triangle.classify(10, 10, 15)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
        self.assertEqual(Triangle.classify(10, 15, 10), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(15, 10, 10), Triangle.Type.ISOSCELES)


    
    # Add more test cases for other statements

if __name__ == '__main__':
    unittest.main()

