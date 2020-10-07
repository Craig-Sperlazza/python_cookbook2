from typing import List, Optional

# project-3
# Author: Craig Sperlazza
# Date: 1/16/2020
# Description: This creates a Library simulator involving multiple classes.
# The three main classes are LibraryItem, Patron and Library classes.
# There are an additional three classes that inherit from LibraryItem
# These three classes that inherit from LibraryItem are Book, Album and Movie.

class LibraryItem:
    """Creates a Library class that contains five private data members,
        id_code, title, checked_out_by, requested_by, and new item location
        The Library Class also has get and set methods for all 5 data members"""

    def __init__(self, id_code: str, title: str) -> None:
        """Initializes 5 data members:
            id_code and title from input;
            checked_out_by and requested_by to None, and
             new item location to ON_SHELF.
        New_item location has three possible string values:
            "ON_SHELF", "ON_HOLD_SHELF", or "CHECKED_OUT" """
        self._id_code: str = id_code #this code will be unique
        self._title: str = title #will not be unique
        self._checked_out_by: None = None
        self._requested_by: None = None
        self._location: str = "ON_SHELF" #starting location is always: ON_SHELF
        self._date_checked_out = 0

    def __str__(self) -> str:
        return ''.join([
            'LibraryItem(',
            f'id_code={self._id_code}, ',
            f'title={self._title}, ',
            f'checked_out_by={self._checked_out_by}, ',
            f'requested_by={self._requested_by}, ',
            f'location={self._location}',
            ')'
        ])

    def get_id_code(self) -> str:
        """Returns the item id_code"""
        return self._id_code

    def get_title(self) -> str:
        """Returns the item title"""
        return self._title

    def get_checked_out_by(self) -> None:
        """Returns None if the item is not checked out.
            Returns the Patron if the item is checked out """
        return self._checked_out_by

    def get_requested_by(self) -> None:
        """Returns None if the item is not requested by a Patron.
            Returns the Patron if the item is requested.
            An item may be requested by only one Patron at a time"""
        return self._requested_by

    def get_location(self) -> str:
        """Returns  the item location which may be one of the following
        "ON_SHELF", "ON_HOLD_SHELF", or "CHECKED_OUT" """
        return self._location

    def get_date_checked_out(self) -> int:
        """when a LibraryItem is checked out, date_checked_out will be set
        to the current_date of the Library"""
        return self._date_checked_out

    def set_checked_out_by(self, mem_ID) -> None:
        """Updates the _checked_out_by member to reflect the member's _id_num
        of the member who checked the item out  """
        self._checked_out_by = mem_ID

    def set_location(self, location_str) -> None:
        """Updates the _checked_out_by member to reflect the member's _id_num
        of the member who checked the item out  """
        self._location = location_str

    def set_date_checked_out(self, current_date) -> None:
        """Updates the date_checked_out_ to reflect the current date of the
        library when the item was checked"""
        self._date_checked_out = current_date

    def set_requested_by(self, status) -> None:
        """Initially set at None. When the item is requested by a Patron,
         requested by will update to the patrons id_num. When the patron
         receives the item, it will go back to None.
        An item may be requested by only one Patron at a time"""
        if self._requested_by == None:
            self._requested_by = status
        elif self._requested_by != None:
            if status == None:
                self._requested_by = None
            else:
                self._requested_by = self._requested_by


class Book(LibraryItem):
    """Creates a Book class that inherits from LibraryItem Class.
        Book uses  the super().__init__ () method to inherit
        the id_code and title and also adds an author parameter.
        Therefore, Book initializes 3 data members: id_code, title, and author.
        Book also implements a method called  get_check_out_length that
        returns the number of days the Book may be checked out for, 21 days"""

    def __init__(self, id_code: str, title: str, author: str) -> None:
        """Book class inherits from LibraryItem. Book uses .super () to
        inherit the __init__ method but, also adds an author parameter.
        Book initializes 3 data members: id_code, title, and author.
        Book also implements a method called  get_check_out_length that
        returns the number of days the Book may be checked out for, 21 days
        Finally, Book also has a get_author method to return the Author"""
        super().__init__(id_code, title)
        self._author: str = author


    def __str__(self) -> str:
        return ''.join([
            'Book(',
            f'id_code={self._id_code}, ',
            f'title={self._title}, ',
            f'author={self._author}, ',
            ')'
        ])

    def get_author(self) -> str:
        """Returns the book author"""
        return self._author

    def get_check_out_length(self) -> int:
        """This returns the number of days a book may be check out for, which is
        21 days"""
        #return self.album_check_out_time
        return 21


class Album(LibraryItem):
    def __init__(self, id_code: str, title: str, artist: str) -> None:
        """Album class inherits from LibraryItem. Album uses .super () to
        inherit the __init__ method but, also adds an artist parameter.
        Album initializes 3 data members: id_code, title, and artist.
        Album also implements a method called  get_check_out_length that
        returns the number of days the Album may be checked out for, 14 days
        Finally, Album also has a get_artist method to return the artist"""
        super().__init__(id_code, title)
        self._artist: str = artist


    def __str__(self) -> str:
        return ''.join([
            'Album(',
            f'id_code={self._id_code}, ',
            f'title={self._title}, ',
            f'artist={self._artist}, ',
            ')'
        ])

    def get_artist(self) -> str:
        """Returns the music artist"""
        return self._artist

    def get_check_out_length(self) -> int:
        """This returns the number of days an album may be checked out for,
        which is 14 days"""
        return 14


class Movie(LibraryItem):
    def __init__(self, id_code: str, title: str, director: str) -> None:
        """Movie class inherits from LibraryItem. Movie uses .super () to
        inherit the __init__ method but, also adds a director parameter.
        Movie initializes 3 data members: id_code, title, and director.
        Movie also implements a method called get_check_out_length that
        returns the number of days the Movie may be checked out for, 7 days
        Finally, Movie also has a get_director method to return the director"""
        super().__init__(id_code, title)
        self._director: str = director

    def __str__(self) -> str:
        return ''.join([
            'Movie(',
            f'id_code={self._id_code}, ',
            f'title={self._title}, ',
            f'director={self._director}, ',
            ')'
        ])

    def get_director(self) -> str:
        """Returns the movie director"""
        return self._director

    def get_check_out_length(self) -> int:
        """This returns the number of days a movie may be checked out for,
        which is 7 days"""
        return 7


class Patron:
    """Creates a Patron class that contains four private data members,
    id_num (unique id code for patron), name (name of patron),
    checked_out_item(a list of checked out items by id_code),
    and fine_amount (holds the amount of overdue charges for the patron)
    The Patron Class also has get and set methods for all 5 data members
    In addition, the Patron class has three other methods:
    1: add_library_item: adds an item from checked_out_item list
    2: remove_library_item: removes an item from checked_out_item list
    3: amend_fine: reduces or increases the fine_amount"""

    def __init__(self, id_num: str, name: str) -> None:
        """Initializes a unique id_num and name of a library patron"""
        self._id_num: str = id_num  # can assume id is unique
        self._name: str = name  # can NOT assume id is unique
        self._checked_out_items: List[str] = [] #a list of Items checked out
        self._fine_amount: float = 0

    def __str__(self) -> str:
        return ''.join([
            'Customer(',
            f'id_num={self._id_num}, ',
            f'name={self._name}, ',
            f'checked_out_items={self._checked_out_items}',
            f'fine_amount={self._fine_amount}',
            ')'
        ])

    def get_id_num(self) -> str:
        """Returns the patron's id_num"""
        return self._id_num

    def get_name(self) -> str:
        """Returns the Patron's name"""
        return self._name

    def get_checked_out_items(self) -> List[str]:
        """Returns the List of the Patorn's checked out items"""
        return self._checked_out_items

    def get_fine_amount(self) -> float:
        """Returns the Patron's name"""
        return self._fine_amount

    def add_library_item(self, id_num: str) -> None:
        """adds item id_num to the patron's account"""
        self._checked_out_items.append(id_num)

    def remove_library_item(self, id_num: str) -> None:
        """removes the product id_num from the patron's account"""
        self._checked_out_items.remove(id_num)

    def amend_fine(self, amend_fine_amount: float):
        """Amends the fine amount of a patron. This accepts a negative amount,
        which decreases the fine amount; or a positive amount, which increases
        the fine amount."""
        self._fine_amount = self._fine_amount + amend_fine_amount


class Library:
    """Creates a Library class that contains 3 private data members,
    a holdings list (which will comprise a list of initialized
    libraryItem Objects, a member list (which will comprise a list of
    initialized Patron Objects, and a date represented by an integer, which
    is initially set to 0. The library class also contains get and set methods
    for all of its data members. There are also the following methods:
    get_library_item-searches the holdings_list to determine in the item exists
    get_member_from_ID-searches the member to list to see if member exists
    check_out_library_item-takes a holding and member id and adds product to
        the customers cart
    return_library_item-takes a product id and returns the item to the library
    request_library_item: takes a product id and member id then checks if item
        was requested, if not it adds the member's request
    pay_fine: takes member id and payment amount and reduces the fine balance
    increment_current_date: this method increments the current date of the
        library by 1 and then iterates through the member list, product list and
        member account list and adds a .10 cents per day fine for each item
        overdue"""

    def __init__(self) -> None:
        """Initializes a holdings list (which will comprise a list of intialized
        libraryItem Objects, a member list (which will comprise a list of
        initialized Patron Objects, and a date represented by an integer, which
         is initially set to 0"""
        self._holdings_lst: List[LibraryItem] = []
        self._member_lst: List[Patron] = []
        self._current_date: int = 0 #initializes at 0 when the library object is
                                    #created, then stores date as it increments


    def __str__(self) -> str:
        return ''.join([
            'Customer(',
            f'holdings_lst={self._holdings_lst}, ',
            f'member_lst={self._member_lst}, ',
            f'current_date={self._current_date}, ',
            ')'
        ])

    def get_member_lst(self) -> object:
        """Returns member list"""
        return self._member_lst

    def get_holdings_lst(self) -> object:
        """Returns library holdings list"""
        return self._holdings_lst

    def get_current_date(self) -> int:
        """Returns current_date"""
        return self._current_date

    def add_library_item(self, holding_obj) -> None:
        """This adds a library holding object to Library holdings list"""
        self._holdings_lst.append(holding_obj)

    def add_patron(self, patron_obj) -> None:
        """This adds a patron object to the Library's member list"""
        self._member_lst.append(patron_obj)

    def get_library_item(self, item_ID: str):
        """returns the library item with the matching ID in the holdings list.
        If no matching ID is found, it returns the special value None"""
        for i in self._holdings_lst:
            if i.get_id_code() == item_ID:
                return i
        return None

    def get_member_from_ID(self, member_ID: str):
        """returns the Patron with the matching ID in the member list.
        If no matching ID is found, it returns the special value None"""
        for m in self._member_lst:
            if m.get_id_num() == member_ID:
                return m
        return None

    def check_out_library_item(self, mem_ID: str, item_ID: str) -> None:
        """adds a desired item (using item id_code) to a specific member's cart
        using the members id_num"""
        item = self.get_library_item(item_ID)
        member = self.get_member_from_ID(mem_ID)

        if item is None:
            return "item not found"
            #print("item not found")

        if member is None:
            return "patron not found"

        if item.get_checked_out_by() is not None:
            return "item already checked out"

        if item.get_requested_by() is not None:
            return "item on hold by other patron"

        else:
            item.set_checked_out_by(mem_ID)
            #Updates the checked_out_by member to reflect the member's _id_num

            item.set_location("CHECKED_OUT")
            #sets the location to checked out

            item.set_date_checked_out(self._current_date)
            #Updates the date_checked_out_to reflect the current date of library

            item.set_requested_by(None)

            member.add_library_item(item_ID)
            #print("OK")
            return "check out successful"

    def return_library_item(self, item_ID: str) -> None:
        """returns a desired item (using item id_code) from a member's cart
        back to the library using the members id_num"""
        item = self.get_library_item(item_ID)

        if item is None:
            # invalid item id (None value) triggers the return statement
            return "item not found"
            #print("item not found")

        if item.get_checked_out_by() is None:
            #if the item is not checked out (None) triggers return statement
            return "item already in library"

        else:
            #Updates the checked_out_by member to reflect the member's _id_num
            for m in self._member_lst:
                if m.get_id_num() == item.get_checked_out_by():
                    member_num = m.get_id_num()
                    #assigns member to the correct patron id
                    member = self.get_member_from_ID(member_num)

                    if item.get_requested_by() is None: #Item was NOT requested
                        item.set_checked_out_by(None)
                        # Updates item's checked_out_by member to reflect None

                        item.set_location("ON_SHELF")
                        #updates the item location to on shelf

                        member.remove_library_item(item.get_id_code())
                        #removes the item from member's checked out items list

                    else:
                        item.set_checked_out_by(None)
                        # Updates item's checked_out_by member to reflect None

                        item.set_location("ON_HOLD_SHELF")
                        # updates the item location to on shelf

                        member.remove_library_item(item.get_id_code())
                        # removes item from the member's checked out items list
            #print("Return successful")
            return "Return Successful"


    def request_library_item(self, mem_ID: str, item_ID: str) -> None:
        """requests an item (using item id_code) to a specific member's cart
        using the members id_num. This function ensures the item number and
        member id number are valid. It also checks to ensure that the item has
        not already been checked out"""
        item = self.get_library_item(item_ID)
        member = self.get_member_from_ID(mem_ID)

        if item is None:
            return "item not found"
            #print("item not found")

        if member is None:
            return "patron not found"

        if item.get_requested_by() is not None:
            return "item already on hold"

        else:
            item.set_requested_by(mem_ID)
            #Updates the item_requested_by to reflect the member's id_num

            if item.get_location() == "ON_SHELF":
                #This checks to see if the status is: "ON_SHELF", if it is, this
                # updates to "ON_HOLD_SHELF"
                item.set_location("ON_HOLD_SHELF")
                return "request successful"
            else:
                return "request successful"

    def pay_fine(self, mem_ID: str, fine_payment: int):
        """Takes as parameters a member's id and a payment amount.
        This function then reduces the member's fine amount using the amend_fine
         function"""
        member = self.get_member_from_ID(mem_ID)
        pay_fine_negative = -fine_payment
        #this reduces the fine amount by making the payment negative

        if member is None: #ensure the member id entered is valid
            #print("no id")
            return "patron not found"

        else:
            member.amend_fine(pay_fine_negative)
            #print(pay_fine_negative)
            #print(member.get_fine_amount(), "zzz")
            return "payment successful"

    def increment_current_date(self) -> None:
        """This method will increment the current_date by 1. The current_date
         was initialized at 0 at the start of the library. This function will
         also implement a loop to loop through the member's list and update
         any fine amounts according to type: book over 21 days,
         movie over 7 days and album over 14 days"""
        self._current_date += 1
        #print(self.get_current_date())
        for m in self._member_lst:
            member = self.get_member_from_ID(m.get_id_num())
            for i in member.get_checked_out_items():
                for p in self._holdings_lst:
                    holding = self.get_library_item(p.get_id_code())
                    if holding.get_id_code() == i:
                        if self._current_date > (holding.get_date_checked_out() + holding.get_check_out_length()):
                            m.amend_fine(.10)


#############TESTING BELOW######################################################

"""
b1 = Book("123", "War and Peace", "Tolstoy")
b2 = Book("234", "Moby Dick", "Melville")
b3 = Book("345", "Phantom Tollbooth", "Juster")
p1 = Patron("abc", "Felicity")
p2 = Patron("bcd", "Waldo")
lib = Library()
lib.add_library_item(b1)
lib.add_library_item(b2)
lib.add_library_item(b3)
lib.add_patron(p1)
lib.add_patron(p2)
lib.check_out_library_item("bcd", "234")
for i in range(7):
    lib.increment_current_date()
lib.check_out_library_item("bcd", "123")
lib.check_out_library_item("abc", "345")
for i in range(24):
    lib.increment_current_date()


lib.pay_fine("bcd", 0.4)

p1Fine2 = p1.get_fine_amount()
p2Fine2 = p2.get_fine_amount()
print(p2Fine2)
print(p1Fine2)
"""



"""
b1 = Book("345", "Phantom Tollbooth", "Juster")
a1 = Album("456", "...And His Orchestra", "The Fastbacks")
m1 = Movie("567", "Laputa", "Miyazaki")


print(b1.get_author())
print(b1.get_title())
print(b1.get_location())
print(b1.get_check_out_length())
print(b1.get_id_code())

print(a1.get_artist())
print(a1.get_title())
print(a1.get_location())
print(a1.get_check_out_length())
print(a1.get_id_code())

print(m1.get_director())
print(m1.get_title())
print(m1.get_location())
print(m1.get_check_out_length())
print(m1.get_id_code())
"""
"""
p1 = Patron("abc", "Felicity")
#print(p1.get_id_num())
#print(p1.get_name())
#print(p1.get_checked_out_items())
#print(p1.get_fine_amount())

p2 = Patron("bcd", "Waldo")
"""
"""
print(p2.get_id_num())
print(p2.get_name())
print(p2.get_checked_out_items())
print(p2.get_fine_amount())

p1.add_library_item("345")
print(p1.get_checked_out_items())

p1.remove_library_item("345")
print(p1.get_checked_out_items())


p1.amend_fine(2.50)
print(p1.get_fine_amount())
p1.amend_fine(-1.00)
print(p1.get_fine_amount())
"""
"""
lib = Library()
lib.add_library_item(b1)
lib.add_library_item(a1)
lib.add_library_item(m1)

lib.add_patron(p1)
lib.add_patron(p2)

lib.check_out_library_item("bcd", "456")
lib.check_out_library_item("bcd", "567")
lib.check_out_library_item("abc", "345")
#print(p2.get_checked_out_items())
#print(a1.get_location())
#print(lib.get_current_date())
#print(a1.get_date_checked_out())
"""
"""
lib.return_library_item("456")
print(a1.get_location())
print(p2.get_checked_out_items())

lib.pay_fine("bcd", 0.4)
#print(p1.get_fine_amount())
"""
"""
for i in range (36):
    lib.increment_current_date()
#print(lib.get_current_date())

#lib.check_out_library_item("bcd", "567")
print(p2.get_checked_out_items())
#print(a1.get_location())
print(lib.get_current_date())
print(m1.get_date_checked_out())
p2_fine = p2.get_fine_amount()
print(p2_fine)
p1_fine = p1.get_fine_amount()
print(p1_fine)


print('==== Begin Library Product List ====')
for p in lib.get_holdings_lst():
    print(p)
print('==== End Library Product List ====')

print('==== Begin Library Member List ====')
for m in lib.get_member_lst():
    print(m)
print('==== End Library Member List ====')

#lib.check_out_library_item("bcd", "456")
"""
"""

def main():


if __name__ == '__main__':
    #main()

    b1 = Book("345", "Phantom Tollbooth", "Juster")
    #a1 = Album("456", "...And His Orchestra", "The Fastbacks")
    #m1 = Movie("567", "Laputa", "Miyazaki")
    print(b1.get_author())
    #print(a1.get_artist())
    #print(m1.get_director())

    p1 = Patron("abc", "Felicity")
    p2 = Patron("bcd", "Waldo")

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

    #print(result)
    #print(result2)

    print('==== Begin Store Product List ====')
    for p in myStore.get_product_lst():
        print(p)
    print('==== End Store Product List ====')

    print('==== Begin Store Member List ====')
    for m in myStore.get_member_lst():
        print(m)
    print('==== End Store Member List ====')
"""
"""
One limited example of how your classes might be used is:

      b1 = Book("123", "War and Peace", "Tolstoy")
      b2 = Book("234", "Moby Dick", "Melville")
      b3 = Book("345", "Phantom Tollbooth", "Juster")
      p1 = Patron("abc", "Felicity")
      p2 = Patron("bcd", "Waldo")
      lib = Library()
      lib.add_library_item(b1)
      lib.add_library_item(b2)
      lib.add_library_item(b3)
      lib.add_patron(p1)
      lib.add_patron(p2)
      lib.check_out_library_item("bcd", "234")
      for i in range(7):
         lib.increment_current_date()
      lib.check_out_library_item("bcd", "123")
      lib.check_out_library_item("abc", "345")
      for i in range(24):
         lib.increment_current_date()
      lib.pay_fine("bcd", 0.4)
      p1Fine = p1.get_fine_amount()
      p2Fine = p2.get_fine_amount()
This example obviously doesn't include all of the functions described above. You are responsible for testing all of the required functions to make sure they operate as specified.
"""
