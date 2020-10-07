import unittest
from Store import Customer, Product, Store, InvalidCheckoutError

# project-2
# Author: Craig Sperlazza
# Date: 1/8/2020
# Description: Main file named Store creates a primitive storefront using
# product, customer, and store classes. This file named StoreTester
# will provide unit testing.

class TestProjects(unittest.TestCase):
    """Defines unit tests for Store.py Note that class TestProjects
    inherits from the unittest module, TestCase class"""

    def test_1(self):
        """test to see if the total charge is correct with shipping costs added"""
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        c1 = Customer("Yinsheng", "QWF", False)
        myStore = Store()
        myStore.add_product(p1)
        myStore.add_member(c1)
        myStore.add_product_to_member_cart("889", "QWF")
        result = myStore.check_out_member("QWF")
        self.assertAlmostEqual(result, 35.7915)

    def test_2(self):
        """#note if we have a improper member id it  raises the error,
         satisfying the test"""
        with self.assertRaises(InvalidCheckoutError):
            p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
            c1 = Customer("Yinsheng", "QWF", False)
            myStore = Store()
            myStore.add_product(p1)
            myStore.add_member(c1)
            myStore.add_product_to_member_cart("889", "QWF")
            result = myStore.check_out_member("WWW") #wrong id

    def test_3(self):
        """test to determine if totals are correct with free shipping"""
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 42.80, 8)
        c1 = Customer("Yinsheng", "QWF", True)
        myStore = Store()
        myStore.add_product(p1)
        myStore.add_member(c1)
        myStore.add_product_to_member_cart("889", "QWF")
        result = myStore.check_out_member("QWF")
        self.assertAlmostEqual(result, 42.80)

    def test_4(self):
        """test to determine if totals are correct with free shipping but adding
        two products"""
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 42.80, 8)
        p2 = Product("723", "Cup", "large cup", 10.20, 2)
        c1 = Customer("Yinsheng", "QWF", True)
        myStore = Store()
        myStore.add_product(p1)
        myStore.add_product(p2)
        myStore.add_member(c1)
        myStore.add_product_to_member_cart("889", "QWF")
        myStore.add_product_to_member_cart("723", "QWF")
        result = myStore.check_out_member("QWF")
        self.assertAlmostEqual(result, 53.00)

    def test_5(self):
        """test to determine if item id was added to cart"""
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 42.80, 8)
        c1 = Customer("Yinsheng", "QWF", True)
        myStore = Store()
        myStore.add_product(p1)
        myStore.add_member(c1)
        myStore.add_product_to_member_cart("889", "QWF")
        result = myStore.check_out_member("QWF")
        member_cart = c1.get_member_cart() #the list of items in member cart
        prod_id_str = ''.join(member_cart) #need a string for assertIn test

        self.assertIn(prod_id_str, "889")

if __name__ == '__main__':
    unittest.main()

