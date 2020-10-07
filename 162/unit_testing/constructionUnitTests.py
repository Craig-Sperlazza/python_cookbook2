import unittest
from constructionProject import RegularProject, NegativeParameterError

class TestProjects(unittest.TestCase): #class TestProjects inherits from unittest module, TestCase class
    """Defines unit tests for RegularProject"""

    def test_1(self):
        proj = RegularProject(1800, 5000, 2000)
        bill = proj.bill_amount()
        self.assertAlmostEqual(bill, 151000)

    def test_2(self):
        with self.assertRaises(NegativeParameterError):
            proj = RegularProject(100, 100, -100) #note if we have a negative it raises the error, hence satisfying the test

if __name__ == '__main__':
    unittest.main()
