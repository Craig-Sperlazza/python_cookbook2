from typing import List, Optional

# project-2
# Author: Craig Sperlazza
# Date: 1/8/2020
# Description: Creating a primitive storefront using product, customer, and
# store classes. The project will also employ a separate file named StoreTester
# in order to provide unit testing.

class InvalidCheckoutError(Exception):
    pass


class Product:
    """Creates a Product class that contains five private data members,
    id_code, title, description, price, and quantity_available."""

    def __init__(self, id_code: str, title: str, description: str, price: float, quantity_available: int) -> None:
        """Initializes 5 private data members id_code, title, description,
        price, quantity_available"""
        self._id_code: str = id_code
        self._title: str = title
        self._description: str = description
        self._price: float = price
        self._quantity_available: int = quantity_available

    def __str__(self) -> str:
        return ''.join([
            'Product(',
            f'id_code={self._id_code}, ',
            f'title={self._title}, ',
            f'description={self._description}, ',
            f'price={self._price}, ',
            f'quantity_available={self._quantity_available}',
            ')'
        ])

    def get_id_code(self) -> str:
        """Returns the product id_code"""
        return self._id_code

    def get_title(self) -> str:
        """Returns the product title"""
        return self._title

    def get_description(self) -> str:
        """Returns the product description"""
        return self._description

    def get_price(self) -> float:
        """Returns the product price"""
        return self._price

    def get_quantity_available(self) -> int:
        """Returns the product quantity"""
        return self._quantity_available

    def decrease_quantity(self) -> None:
        """Decreases the quantity_available by 1"""
        if self._quantity_available > 0:
            self._quantity_available -= 1


class Customer:
    """Creates a Customer class that contains three private data members,
    name, account_ID, and whether the customer is a premium_member. The class
    also creates a customer cart to which products can be added, emptied, etc."""

    def __init__(self, name: str, account_ID: str, premium_member: bool) -> None:
        """Initializes private data members name, account id, premium member,
         and member cart (which is a list to add items to)"""
        self._name = name
        self._account_ID: str = account_ID
        self._premium_member: bool = premium_member
        self._member_cart: List[int] = []

    def __str__(self) -> str:
        return ''.join([
            'Customer(',
            f'name={self._name}, ',
            f'account_ID={self._account_ID}, ',
            f'premium_member={self._premium_member}, ',
            f'member_cart={self._member_cart}',
            ')'
        ])

    def get_account_ID(self) -> str:
        """Returns the customer's account_ID"""
        return self._account_ID

    def get_name(self) -> str:
        """Returns the customer's name"""
        return self._name

    def get_premium_member(self) -> bool:
        """Returns premium_member status"""
        return self._premium_member

    def get_member_cart(self) -> List[int]:
        """Returns member cart"""
        return self._member_cart

    def is_premium_member(self) -> bool:
        """Checks whether the customer is a premium member (free shipping)"""
        return self.get_premium_member()

    def add_product_to_cart(self, id_code: int) -> None:
        """adds product id_code to the customer's cart"""
        self._member_cart.append(id_code)

    def empty_cart(self) -> None:
        """empties the Customer's cart"""
        self._member_cart.clear()


class Store:
    """Creates a Store class that contains three private data members,
    product list, member list (both of which will store the product and customer
    objects respectively) and a search list used to store search results"""

    def __init__(self) -> None:
        """Initializes 3 private data members product list, member list
        (both of which will store the product and customer
        objects respectively) and a search list used to store search results"""
        self._product_lst: List[Product] = []
        self._member_lst: List[Customer] = []
        self._search_lst: List = []

    def get_member_lst(self) -> List[Customer]:
        """Returns member list"""
        return self._member_lst

    def get_product_lst(self) -> List[Product]:
        """Returns product list"""
        return self._product_lst

    def get_search_lst(self) -> List:
        """Returns search list"""
        return self._search_lst

    def add_product(self, product_obj: Product) -> None:
        """This passes a product object to a product list in the store"""
        self._product_lst.append(product_obj)

    def add_member(self, member_obj: Customer) -> None:
        """This passes a member object to a member list in the store"""
        self._member_lst.append(member_obj)

    def get_product_from_ID(self, product_ID: int) -> Optional[Product]:
        """returns the Product with the matching ID.
        If no matching ID is found, it returns the special value None"""
        for p in self._product_lst:
            if p.get_id_code() == product_ID:
                return p
        return None

    def get_member_from_ID(self, member_ID: str) -> Optional[Customer]:
        """returns the Customer with the matching ID.
        If no matching ID is found, it returns the special value None"""
        for m in self._member_lst:
            if m.get_account_ID() == member_ID:
                return m
        return None

    def product_search(self, search_term: str) -> List[int]:
        """returns a sorted list of ID codes for every product whose title or
        description contains the search string."""

        self._search_lst.clear()
        #print(search_term)
        search_cap = search_term.capitalize()
        for i in self._product_lst:
            if search_term in i.get_description() or search_cap in i.get_description():
                self._search_lst.append(i.get_id_code())
        for i in self._product_lst:
            if search_term in i.get_title() or search_cap in i.get_title():
                self._search_lst.append(i.get_id_code())
        self._search_lst.sort()
        set_lst = set(self._search_lst) #gets rid of duplicates
        self._search_lst = list(set_lst)
        return self._search_lst
        #return set_lst

    def add_product_to_member_cart(self, prod_ID: int, mem_ID: str) -> None:
        """adds a desired product to a specific member's cart"""
        product = self.get_product_from_ID(prod_ID)
        member = self.get_member_from_ID(mem_ID)

        if member is None:
            return "member ID not found"

        if product is None:
            return "product ID not found"

        if product.get_quantity_available() > 0:
            #product.decrease_quantity()
            member.add_product_to_cart(prod_ID)
            return "product added to cart"

        else:
            return "product out of stock"


    def check_out_member(self, mem_ID: str) -> None:
        """Checks to make sure there is a valid customer, product and then
        computes total"""
        total = 0
        total_with_shipping = 0
        #product = self.get_product_from_ID(prod_ID)
        member = self.get_member_from_ID(mem_ID)

        if member is None:
            raise InvalidCheckoutError
        else:
            for i in member.get_member_cart():
                for j in self._product_lst:
                    if j.get_id_code() == i and j.get_quantity_available() > 0:
                        total = total + j.get_price()
                        prod_id = j.get_id_code()
                        #print(j.get_id_code(), "xxx")
                        #print(prod_id, "yyy")
                        product = self.get_product_from_ID(prod_id)
                        product.decrease_quantity()
                        if member.is_premium_member() == True:
                            #print(member)
                            #print(total)
                            total_with_shipping = total

                        else:
                            total_with_shipping = total + (total * .07)
                            #print(member)
                            #print(total_with_shipping)
            return total_with_shipping


def main():
    try:
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        c1 = Customer("Yinsheng", "QWF", False)
        myStore = Store()
        myStore.add_product(p1)
        myStore.add_member(c1)
        myStore.add_product_to_member_cart("889", "QWF")
        result = myStore.check_out_member("QWF")
        print(result)
    except InvalidCheckoutError:
        print("That is an invalid member ID. Please try again")

    try:
        p2 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        c2 = Customer("Yinsheng", "QWF", False)
        myStore = Store()
        myStore.add_product(p2)
        myStore.add_member(c2)
        myStore.add_product_to_member_cart("889", "QWF")
        result = myStore.check_out_member("XYZ") #does not exist
        print(result)
    except InvalidCheckoutError:
        print("That is an invalid member ID. Please try again")


if __name__ == '__main__':
    main()
"""
    p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)

    p2 = Product("3", "rod", "red", 12, 6)

    c1 = Customer("Yinsheng", "QWF", False)

    c2 = Customer("Bob", "WER", True)

    myStore = Store()
    myStore.add_product(p1)
    myStore.add_product(p2)
    myStore.add_member(c1)
    myStore.add_member(c2)
    myStore.add_product_to_member_cart("889", "QWF")
    myStore.add_product_to_member_cart("889", "WER")
    myStore.add_product_to_member_cart("3", "QWF")
    result = myStore.check_out_member("QWF")
    result2 = myStore.check_out_member("WER")

    print(result)
    print(result2)

    print('==== Begin Store Product List ====')
    for p in myStore.get_product_lst():
        print(p)
    print('==== End Store Product List ====')

    print('==== Begin Store Member List ====')
    for m in myStore.get_member_lst():
        print(m)
    print('==== End Store Member List ====')
"""

