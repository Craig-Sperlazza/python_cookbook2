import unittest
from listfuncs import list_max


class TestListMax(unittest.TestCase):  # The class name can be whatever you want
    """
    Contains unit tests for the listMax function
    """

    def test_1(self):  # The function names also can be whatever you want
        a_list = [6, 43, 18, 100, 9, 85]
        result = list_max(a_list)
        self.assertEqual(result, 100)

    def test_2(self):
        a_list = [-7, -1, -38, -2, -99]
        result = list_max(a_list)
        self.assertEqual(result, -1)

    def test_3(self):
        a_list = [-3, 7, 96, -102, 58, 14, -8]
        result = list_max(a_list)
        self.assertEqual(result, 96)

    def test_4(self):
        a_list = [9]
        result = list_max(a_list)
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()