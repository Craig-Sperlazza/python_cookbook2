# linked_list.py
# ===================================================
# Linked list exploration
# Part 1: implement the deque and bag ADT with a Linked List
# Part 2: implement the deque ADT with a CircularlyDoubly-
# Linked List
# ===================================================
# Craig Sperlazza
# Data Structures Assignment 3
# April 25, 2020

'''
**********************************************************************************
Part1: Deque and Bag implemented with Linked List
**********************************************************************************
'''

class SLNode:
    def __init__(self):
        self.next = None
        self.data = None


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a linked list with a head and tail node with None data
        """
        self.head = SLNode()
        self.tail = SLNode()
        self.head.next = self.tail

        # populate list with initial set of nodes (if provided)
        if start_list is not None:
            for data in start_list:
                self.add_back(data)

    def __str__(self):
        """
        Returns a human readable string of the list content of the form
        [value1 -> value2 -> value3]

        An empty list should just return []

        Returns:
            The string of the human readable list representation
        """
        out = '['
        if self.head.next != self.tail:             
            cur = self.head.next.next
            out = out + str(self.head.next.data)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out


    def add_link_before(self, data, index):
        """
        Adds a new link containing data and inserts it before the link at index.
        If index is 0, it inserts at the beginning of the list.

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly added node
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        i = 0
        current = self.head
        previous = self.head

        if index == 0:
            self.add_front(data)
        else:
            while i < index + 1:
                if current.next == self.tail and index >= i + 1:
                    raise Exception ("Index out of bounds")
                elif i == index:
                    new_link.next = current.next
                    current.next = new_link
                    return
                else:
                    previous = current
                    current = current.next
                    i += 1


    def remove_link(self, index):
        """
        Removes the link at the location specified by index
        Args:
            Index: The index of the node that will be removed
        """
        i = 0
        current = self.head
        previous = self.head

        if index < 0:
            raise Exception("Index out of bounds")

        elif index == 0:
            current = current.next
            self.head.next = current.next
        else:
            while i < index + 1:
                if current.next == self.tail and index >= i + 1:
                    raise Exception("Index out of bounds")
                elif i == index:
                    previous = current
                    current = current.next
                    previous.next = current.next
                    return
                else:
                    previous = current
                    current = current.next
                    i += 1


    def add_front(self, data):
        """
        Adds a new node after the head that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        if self.head.next == self.tail:
            #Link the new node to tail
            new_link.next = self.head.next

            # The new node follows head.
            self.head.next = new_link

        else:
            # set the new link next equal to tail
            new_link.next = self.tail
            new_link.next = self.head.next

            # The new node follows head
            self.head.next = new_link

    def add_back(self, data):
        """
        Adds a new node before the tail that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # if self.head.next.data == None:
        #     new_link.next = self.head.next
        #     self.head.next = new_link

        #if the list is empty but for the sentinels
        if self.head.next == self.tail:
            new_link.next = self.head.next #set the new node next to tail
            self.head.next = new_link  #set the head next to the new node
        else:
            new_link.next = self.tail
            current = self.head
            #need to loop through the linked list until you get to the element
            #before the tail
            while current.next != self.tail:
                current = current.next
            current.next = new_link


    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """

        if self.head.next == self.tail:
            return None
        else:
            return self.head.next.data


    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """
        # if the list is empty but for the sentinels
        if self.head.next == self.tail:
            return None
        else:
            current = self.head
            # need to loop through the linked list until you get to the element
            # before the tail
            while current != self.tail:
                if current.next == self.tail:
                    return current.data
                else:
                    current = current.next


    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """

        if self.head.next == self.tail:
            return
        else:
            current = self.head.next
            self.head.next = current.next


    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """

        # if the list is empty but for the sentinels
        if self.head.next == self.tail:
            return
        else:
            current = self.head
            previous = self.head
            # need to loop through the linked list until you get to the element
            # before the tail
            while current != self.tail:
                if current.next == self.tail:
                    previous.next = current.next
                    return
                else:
                    previous = current
                    current = current.next


    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """

        if self.head.next == self.tail:
            return True
        elif self.head.next != self.tail:
            return False

    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """
        #return false if the list is empty
        if self.head.next == self.tail:
            return False
        elif self.head.next != self.tail:
            current = self.head.next
            #if value is the first data node return true
            if current.data == value:
                return True
            else:
                #iterate throough the list
                while current.next != self.tail:
                    current = current.next
                    if current.data == value:
                        return True
                    current = current.next
            return False

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """

        current = self.head
        previous = self.head

        while current.next != self.tail:
            if current.data == value:
                previous.next = current.next
                return
            else:
                previous = current
                current = current.next


'''
**********************************************************************************
Part 2: Deque implemented with CircularlyDoublyLinked List
**********************************************************************************
'''

class DLNode:
    def __init__(self):
        self.next = None
        self.prev = None
        self.data = None

class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a linked list with a single sentinel node containing None data
        """
        self.sentinel = DLNode()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate list with initial set of nodes (if provided)
        if start_list is not None:
            for data in start_list:
                self.add_back(data)

    def __str__(self):
        """
        Returns a human readable string of the list content of the form
        [value1 <-> value2 <-> value3]

        An empty list should just print []

        Returns:
            The string of the human readable list representation
        """
        out = '['
        if self.sentinel.prev != self.sentinel:             
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.data)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out

    def add_link_before(self, data, index):
        """
        Adds a new link containing data and inserts it before the link at index.
        If index is 0, it inserts at the beginning of the list.

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly added node
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        i = 0
        current = self.sentinel
        previous = self.sentinel

        if index == 0:
            self.add_front(data)
        else:
            while i < index + 1:
                if current.next == self.sentinel and index >= i + 1:
                    raise Exception("Index out of bounds")
                elif i == index:
                    after_current = current.next
                    new_link.next = current.next
                    new_link.prev = current
                    after_current.prev = new_link
                    current.next = new_link
                    return
                else:
                    previous = current
                    current = current.next
                    i += 1

    def remove_link(self, index):
        """
        Removes the link at the location specified by index
        Args:
            Index: The index of the node that will be removed
        """

        i = 0
        current = self.sentinel
        previous = self.sentinel

        if index < 0:
            raise Exception("Index out of bounds")

        elif index == 0:
            node_to_remove = current.next
            new_front = node_to_remove.next
            self.sentinel.next = new_front
            new_front.prev = self.sentinel
        else:
            while current.next != self.sentinel:
                if index == i:
                    node_to_remove = current.next
                    current.next = node_to_remove.next
                    current.next.prev = current
                    return
                else:
                    current = current.next
                    i += 1
        # previous = current
        # current = current.next
        # previous.next = current.next
        # current.prev = previous
        # return

                    # # new_current = current.next
                    # # previous.next = new_current
                    # # new_current.prev = previous
                    #
                    # # node_to_remove = current.next
                    # # new_front = node_to_remove.next
                    # # current.next = new_front
                    # # new_front.prev = current
                    # return

    def add_front(self, data):
        """
        Adds a new node at the beginning of the list that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # if the list is empty but for the sentinel
        if self.sentinel.next == self.sentinel:
            new_link.next = self.sentinel  # set the new node next to sentinel(tail)
            new_link.prev = self.sentinel  # set the new node prev to sentinel(head)
            self.sentinel.next = new_link  # set the sentinel next to new node
            self.sentinel.prev = new_link  # set the sentinel prev to new node
        else:
            new_link.prev = self.sentinel
            new_link.next = self.sentinel.next
            self.sentinel.next.prev = new_link
            self.sentinel.next = new_link


    def add_back(self, data):
        """
        Adds a new node at the end of the list that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # if the list is empty but for the sentinel
        if self.sentinel.next == self.sentinel:
            new_link.next = self.sentinel  #set the new node next to sentinel(tail)
            new_link.prev = self.sentinel #set the new node prev to sentinel(head)
            self.sentinel.next = new_link  #set the sentinel next to new node
            self.sentinel.prev = new_link #set the sentinel prev to new node
        else:
            new_link.prev = self.sentinel.prev
            new_link.next = self.sentinel
            self.sentinel.prev.next = new_link
            self.sentinel.prev = new_link


    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """

        if self.sentinel.next == self.sentinel:
            return None
        else:
            return self.sentinel.next.data


    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """

        # if the list is empty but for the sentinels
        if self.sentinel.next == self.sentinel:
            return None
        else:
            return self.sentinel.prev.data


    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """

        # if the list is empty but for the sentinel
        if self.sentinel.next == self.sentinel:
            return
        else:
            first = self.sentinel.next
            new_first = first.next
            new_first.prev = self.sentinel
            self.sentinel.next = new_first


    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """

        # if the list is empty but for the sentinels
        if self.sentinel.next == self.sentinel:
            return
        else:
            last = self.sentinel.prev
            new_last = last.prev
            new_last.next = self.sentinel
            self.sentinel.prev = new_last

    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """

        if self.sentinel.next == self.sentinel:
            return True
        else:
            return False


    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """

        if self.sentinel.next == self.sentinel:
            return False
        elif self.sentinel.next != self.sentinel:
            current = self.sentinel.next
            # if value is the first data node return true
            if current.data == value:
                return True
            else:
                # iterate through the list
                while current.next != self.sentinel:
                    current = current.next
                    if current.data == value:
                        return True
                    current = current.next
            return False

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """
        current = self.sentinel
        previous = self.sentinel

        while current.next != self.sentinel:
            if current.data == value:
                new_current = current.next
                previous.next = current.next
                new_current.prev = previous
                return
            else:
                previous = current
                current = current.next

    def circularListReverse(self):
        """
        Reverses the order of the links. It must not create any additional new links to do so.
        (e.g. you cannot call DLNode()). If the list printed by following next was 0, 1, 2, 3,
        after the call it will be 3,2,1,0
        """
        #empty list
        if self.sentinel.next == self.sentinel:
            return
        #one item
        elif self.sentinel.next.next == self.sentinel:
            return
        else:
            #since we have only one sentinel node that acts as the head and tail
            #we have to differentiate it into two nodes by assigning it variables
            #avoiding an infinite loop so we have a stop point
            sentinel_end = self.sentinel
            current = self.sentinel

            #Next, we switch the next and prev of current (sentinel). We do this
            # seperately since the current and end is technically the same.
            # We need a temporary variable as a placeholder to aid in this.
            # Finally, we will move to the next node
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = current.next

            #now we can iterate down the data list doing the same thing
            # outlined above and stopping once we come to the sentinel
            while current != sentinel_end:
                temp = current.next
                current.next = current.prev
                current.prev = temp
                current = current.next


# #add_back
# list = CircularList()
# list.add_back("C")
# list.add_back("B")
# list.add_back("A")
# print(list)

# #add front
# list2 = CircularList()
# list2.add_front("A")
# list2.add_front("B")
# list2.add_front("C")
# print(list2)

# #get front
# list3 = CircularList([1, 2])
# print(list3.get_front())
# list3.remove_front()
# print(list3.get_front())
# list3.remove_back()
# print(list3.get_front())

# # get back
# list4 = CircularList([1, 2, 3])
# list4.add_back(4)
# print(list4)
# print(list4.get_back())
# list4.remove_back()
# print(list4)
# print(list4.get_back())

# #is empty
# list5 = CircularList([1, 2])
# print(list5.is_empty())
# list5.remove_front()
# list5.remove_back()
# print(list5.is_empty())

# #remove back
# list6 = CircularList()
# list6.remove_back()
# list6.add_front("Z")
# print(list6)
# list6.remove_back()
# print(list6)

# #remove front
# list7 = CircularList([1, 2])
# print(list7)
# list7.remove_front()
# list7.remove_front()
# list7.remove_front()
# print(list7)


# #contains
# list8 = CircularList([1, 2, 3, 3, 5])
# print(list8.contains(20))
# print(list8.contains(3))
# print(list8)
# list8.remove(3)
# print(list8)
# print(list8.contains(5))
# list8.remove(3)
# print(list8)
# print(list8.contains(3))

# #Remove
# list9 = CircularList([1, 3, 3, 4, 3])
# list9.remove(3)
# print(list9)
# list9.remove(20)
# list9.remove(3)
# list9.remove(-2)
# print(list9)
# list9.remove(1)
# print(list9)
#
# # remove Link
# list10 = CircularList([1, 2, 3, 4, 5])
# list10.remove_link(0)
# print(list10)
# list10.remove_link(0)
# print(list10)
# list10.remove_link(0)
# print(list10)
# #list10.remove_link(-2)
#
# # remove Link TESTING 2
# list11 = CircularList([1, 2, 3, 4, 5])
# list11.remove_link(1)
# print(list11) #1, 3, 4, 5
# list11.remove_link(3)
# print(list11) #1, 3, 4
# list11.remove_link(2)
# print(list11) #1, 3
# list11.remove_link(0)
# print(list11) #3

# # add link before
# list12 = CircularList()
# list12.add_link_before("A", 0)
# list12.add_link_before("B", 0)
# list12.add_link_before("C", 1)
# #list12.add_link_before("D", 20)
# print(list12) #B C A

# #circular list
# list = CircularList([1, 2, 3, 3, 4, 5])
# print(list)
# list.circularListReverse()
# print(list)

#SINGLY LINKED TESTING#########################################################
# #remove link----NOT WORKING INDEXING ISSUES I BELIEVE
# list10 = LinkedList([1, 2, 3, 4, 5])
# list10.remove_link(0)
# print(list10)
# list10.remove_link(2)
# print(list10)
# list10.remove_link(0)
# print(list10)
# #list10.remove_link(-2)


# #Remove back
# list = LinkedList()
# list.remove_back()
# list.add_front("Z")
# list.remove_back()
# print(list)

# #Add link before---first two are working (0 index)#####NEEDS WORK##########
# list9 = LinkedList()
# list9.add_link_before("A", 0)
# list9.add_link_before("B", 0)
# list9.add_link_before("C", 1)
# print(list9)
# list9.add_link_before("D", 20)
# print(list9)


# #remove link----NOT WORKING INDEXING ISSUES I BELIEVE
# list10 = LinkedList([1, 2, 3, 4, 5])
# list10.remove_link(0)
# print(list10)
# list10.remove_link(0)
# print(list10)
# list10.remove_link(0)
# print(list10)
# list10.remove_link(-2)


# #get back
# list = LinkedList([1, 2, 3])
# list.add_back(4)
# print(list.get_back())
# list.remove_back()
# print(list)
# print(list.get_back())

#
# #contains
# list0 = LinkedList([1, 2, 3, 3, 5])
# print(list0.contains(20))
# print(list0.contains(3))
# list0.remove(3)
# print(list0.contains(5))
# list0.remove(3)
# print(list0.contains(3))

# ###add back testing---working
# list = LinkedList()
# list.add_back("C")
# list.add_back("B")
# list.add_back("A")
# print(list)


# ###add front testing----working
# list2 = LinkedList()
# list2.add_front("A")
# list2.add_front("B")
# list2.add_front("C")
# print(list2)


# ##get front  is working
# list3 = LinkedList([1, 2])
# print(list3.get_front())
# list3.remove_front()
# print(list3.get_front())
# ####Need to test once remove back is working
# list3.remove_back()
# print(list3.get_front())
# listEmpty = LinkedList([])
# print(listEmpty.get_front())


# ###addback is working ----get back is not
# list4 = LinkedList([1, 2, 3])
# list4.add_back(4)
# list4.add_back(88)
# print(list4)
# print(list4.get_back())


# #####remove_front
# list5 = LinkedList([1, 2])
# print(list5)
# list5.remove_front()
# print(list5)
# list5.remove_front()
# print(list5)


# ####is empty---working
# list6 = LinkedList([1, 2])
# print(list6.is_empty())
# list7 = LinkedList([])
# print(list7.is_empty())


# #remove is working
# list8 = LinkedList([1, 3, 3, 4, 3])
# list8.remove(3)
# print(list8)
# list8.remove(20)
# list8.remove(3)
# list8.remove(-2)
# print(list8)
# list8.remove(1)
# print(list8)


