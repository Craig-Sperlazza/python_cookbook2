import unittest

from employee_class import Employee

class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("Set up class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Tear Down Class")

    def setUp(self) -> None:
        print("Set Up:")
        self.emp1 = Employee("John", "Smith", 1000)
        self.emp2 = Employee("Katie", "Johnson", 15000)
        self.emp3 = Employee("Rhonda", "Jones", 20000)

    def tearDown(self) -> None:
        print("Tear Down")

    def test_full_name(self):
        print("Test full_name")
        self.assertEqual(self.emp2.full_name, "Katie Johnson")

    def test_email(self):
        print("Test Email")
        self.assertEqual(self.emp1.email, "John.Smith@company.com")

    def test_give_raise(self):
        print("Test give raise")
        self.assertEqual(self.emp3.pay, 20000)
        self.emp3.give_raise()
        self.assertEqual(self.emp3.pay, 21000)

if __name__ == "__main__":
    unittest.main()