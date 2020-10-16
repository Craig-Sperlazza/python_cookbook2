#https://www.youtube.com/watch?v=6tNS--WetLI&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=21
#https://docs.python.org/3/library/unittest.html#assert-methods

import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10,5), 15)
        self.assertEqual(calc.add(-1,1), 0)
        self.assertEqual(calc.add(-1,-1), -2)
    
    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5), 5)
        self.assertEqual(calc.subtract(-1,1), -2)
        self.assertEqual(calc.subtract(-1,-1), 0)
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5), 50)
        self.assertEqual(calc.multiply(-1,1), -1)
        self.assertEqual(calc.multiply(-1,-1), 1)
    
    def test_divide(self):
        self.assertEqual(calc.divide(10,5), 2)
        self.assertEqual(calc.divide(-1,1), -1)
        self.assertEqual(calc.divide(-1,-1), 1)

        # checking for the zerodivision error can be done in two ways
        # 1. he prefers context manager:
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

        # 2. self.assertRaises(exceptionWeExpect, functionWeRun, arguments seperated by ,)
        self.assertRaises(ValueError, calc.divide, 10, 0)
        #self.assertRaises(ValueError, calc.divide, 10, 2) #this technically fails the test because it doesnt thrwo error

#use this so you can run the tests directly, if you dont have it
# must run it in commandline as: python -m unittest test_calc.py
if __name__ == "__main__":
    unittest.main()