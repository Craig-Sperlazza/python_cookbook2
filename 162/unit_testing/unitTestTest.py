import unittest
from unitTestExercise import mult3

class TestMult3(unittest.TestCase):
    """testing multiplication function"""

    def test_1(self):
        ret_val = mult3(3, 2, 1)
        self.assertEqual(ret_val, 6)

    def test_2(self):
        ret_val = mult3(3, 2, 1)
        self.assertEqual(ret_val, 8)

if __name__ == '__main__':
    unittest.main()