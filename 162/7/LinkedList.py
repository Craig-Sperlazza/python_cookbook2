# project-7
# Author: Craig Sperlazza
# Date: 2/06/2020
# Description: The program creates a LinkedList class that has recursive
# implementations of:add, display, remove, contains, insert, and reverse methods

class Node:
    """
    Represents a node in a linked list
    """
    def __init__(self, data):
        self.data = data  # holds the value we are storing in the node
        self.next = None  # refers to the next node in the list



class LinkedList:
    """
    A linked list implementation of the List ADT.
    This class initializes only one data member, self.head, which is used to
    keep track of first node in the list. self.head is initially set to None,
    then self.head becomes the reference to the first node in the list
    """
    def __init__(self):
        """self.head is used to keep track of first node in the list.
        Initially set to None, then self.head is the reference to the first
        node in the list
        """
        self.head = None


    def add(self, val):
        """
        add calls helper method named help_add to perform critical work:
        :param accepts as a parameter a value to add to the linked list
        :return:
        Adds a node containing value passed in as a parameter to the linked list
        The add method first checks to see if the list is empty
        (by checking whether head is None).
        If it is empty, then the method creates a new node containing the
        parameter value and assigns it to be the head.
        If the list was not empty, the method sets current equal to head,
        so they refer to the same node.
        Then while there’s still another node in the list,
        it sets current to refer to that node and recursively calls the function
        When it arrives at the last node in the list,
        it creates a new node containing the parameter value and
        makes the (formerly) last node refer to it (with its next data member)
        """
        return self.help_add(val, 0)


    def help_add(self, val, count):
        """
        helper function to perform critical work:
        :param accepts a value to add parameter and an initial count parameter.
        The default count parameter, initially set to zero
        (with no effect on output)  will be set to subsequent current values
        as the function recursively iterates through the list
        :return:
        Adds a node containing value passed in as a parameter to the linked list
        The add method first checks to see if the list is empty
        (by checking whether head is None).
        If it is empty, then the method creates a new node containing the
        parameter value and assigns it to be the head.
        If the list was not empty, the method sets current equal to head,
        so they refer to the same node.
        Then while there’s still another node in the list,
        it sets current to refer to that node and recursively calls the function
        When it arrives at the last node in the list,
        it creates a new node containing the parameter value and
        makes the (formerly) last node refer to it (with its next data member).
        """

        if self.head is None:  # If the list is empty
            self.head = Node(val)
        else:
            if count == 0:
                current_val = self.head
                if current_val.next is None:
                    current_val.next = Node(val)
                else:
                    return self.help_add(val, current_val.next)
            else:
                current_val = count
                if current_val.next is None:
                    current_val.next = Node(val)
                else:
                    return self.help_add(val, current_val.next)


    def display(self):
        """
        Display calls helper method named help_display to perform critical work:
        :param No paramters accepted
        :return:
        Prints out the values in the linked list
        The display method sets current equal to head and then advances through
        the list as in the add method, but it prints out the value in each node
        as it goes. In order to print all the values on a single line,
        it uses an optional parameter that makes it print a space at the end
        instead of a newline.
        """
        return self.help_display(0)


    def help_display(self, count):
        """
        Helper function for display.
        :param Accepts a default count parameter, initially set to zero
        (with no effect on output) but will be set to subsequent current values
        as the function recursively iterates through the list
        :return:
        Prints out the values in the linked list
        The display method sets current equal to head and then advances through
        the list as in the add method, but it prints out the value in each node
        as it goes. In order to print all the values on a single line,
        it uses an optional parameter that makes it print a space at the end
        instead of a newline.
        """
        if count == 0:
            current = self.head
            if current is None:
                print()
            else:
                print(current.data, end=" ")
                return self.help_display(current.next)
        else:
            current = count
            if current is None:
                print()
            else:
                print(current.data, end=" ")
                return self.help_display(current.next)
        #print()


    def remove(self, val):
        """
        remove calls helper method named help_remove to perform critical work:
        :param value to be removed
        :return:
        Removes the node containing value parameter from the linked list
        The remove method first checks to see if the list is empty. If so,
            it simply returns.
        Next it checks to see if the head should be removed.
            If so, it makes head refer to the next node (or None).
        If the list is not empty, and the head is not being removed, then
            the method advances through the list until either current advances
             past the end of the list or the value is found and it is removed by
             being spliced out of the list by making the node behind current
             (which is previous) refer to the node ahead of current
             (which is current.next).
         If the value was not found, then the method does nothing.
        """
        return self.help_remove(val, 0, 0)


    def help_remove(self, val, current_count, previous_count):
        """
        :param val: value to be removed
        :param current_count: default parmeter that will hold current value
        :param previous_count: default parameter that will hold previous value
        :return: Nothing, it simply removes the value from the list
        """
        if self.head is None:  # If the list is empty
            return
        if self.head.data == val:  # If the node to remove is the head
            self.head = self.head.next

        if current_count == 0:
            current_count = self.head
            previous_count = current_count
            if current_count is not None and current_count.data == val:
                previous_count.next = current_count.next
            elif current_count is not None and current_count.data != val:
                current_count2 = current_count.next
                return self.help_remove(val, current_count2, current_count)
            else:
                return
        else:
            current_count = current_count
            previous_count = previous_count
            if current_count is not None and current_count.data == val:
                previous_count.next = current_count.next
            elif current_count is not None and current_count.data != val:
                current_count2 = current_count.next
                return self.help_remove(val, current_count2, current_count)
            else:
                return


    def is_empty(self):
        """
        :param: no parameters
        :return
        Returns True if the linked list is empty (i.e. the head equals None),
        Returns False otherwise
        """
        return self.head is None


    def contains(self, key):
        """
        Utilizes a helper function named help_contains
        :param
        Takes a value to search for as a parameter
         :return True if that value is in the linked list,
         and returns False otherwise.
        """
        return self.help_contains(key, 0)


    def help_contains(self, key, count):
        """
        :param accepts as a paramters a value to check for in the list
        Also accepts a default count parameter, initially set to zero
        (with no effect on output) but will be set to subsequent current values
        as the function recursively iterates through the list
        :return:
        Returns True if that value is in the linked list,returns False otherwise
        """
        if self.head is None:  # If the list is empty
            #print(False)
            return False

        if count == 0:
            current = self.head
            if current is not None and current.data == key:
                #print(True)
                return True
            elif current is not None and current.data != key:
                current = current.next
                return self.help_contains(key, current)
            else:
                #print(False)
                return False
        else:
            current = count
            if current is not None and current.data == key:
                #print(True)
                return True
            elif current is not None and current.data != key:
                current = current.next
                return self.help_contains(key, current)
            else:
                #print(False)
                return False


    def reverse(self):
        """
        reverse calls helper method named help_reverse to perform critical work:
        :param accepts no parameters
        :return:
        reverses the linked list but does not return anything

        :Note: reverse does initialize both the curr and prev values prior to
        calling the helper function. This program attempted to do all the work
        in the helper function but it kept running into an infinite recursion.
        Keeping these two values initialized outside the helper recursion
        solved this problem
        """
        curr = self.head
        prev = None
        return self.help_reverse(curr, prev)


    def help_reverse(self, curr, prev):
        """
        Reverse method takes no parameters (besides self) and doesn't return a
        value,it simply reverses the order of the nodes in the linked list.
        """
        if curr is None:  # If the list is empty
            return
        #if current.next == None:  # If the list has 1 item
            #return
        if curr is not None:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        self.head = prev
        return self.help_reverse(curr, prev)


    def insert(self, data, position):
        """
        method named insert that takes as parameters a value and a position.
        A position of zero means that the new value will become the new first
        element.
        A position of one means it will become the new second element, etc.
        A position >= the length of the list means it will be added at the
        end of the list.
        """
        return self.help_insert(data, position, 0, 0, 0)


    def help_insert(self, data, position, count, previous, current_position):
        """
        method named insert that takes as parameters a value and a position.
        A position of zero means that the new value will become the
        new first element.
        A position of one means it will become the new second element, etc.
        A position >= the length of the list means it will be added at the
        end of the list.
        """
        node = Node(data)
        if self.head == None:  # if an empty list, new node becomes the head
            self.head = node
            return
        if position == 0:  # if position 0 is entered, make the new node the head
            node.next = self.head  # previous head becomes our new node/new heads reference
            self.head = node
            return
        if count == 0:
            current = self.head
            previous = current
            current_position = current_position + 1
            current = current.next
            return self.help_insert(data, position, current, previous, current_position)
        else:
            current = count
            if current_position == position:
                previous.next = node
                node.next = current
            elif current_position < position and current.next != None:
                previous = current
                current_position = current_position + 1
                current = current.next
                return self.help_insert(data, position, current, previous, current_position)
            elif current_position < position and current.next == None:
                node.next = None
                current.next = node
                return

"""
# Remember that with the main function and the if statement, this code only executes if
# it is being run as a script, if you are importing it it will not run.

def main():
    my_list = LinkedList()
    my_list.reverse()
    my_list.display()
    my_list.add(1)
    my_list.reverse()
    my_list.display()
    my_list.add(2)
    my_list.reverse()
    my_list.display()
    my_list.add(3)
    my_list.display()
    my_list.remove(1)
    my_list.remove(2)
    my_list.remove(3)
    my_list.display()
    my_list.is_empty()
    my_list.contains(1)
    my_list.add(13)
    my_list.contains(13)
    my_list.add(9)
    my_list.add(81)
    my_list.display()
    my_list.remove(13)
    my_list.display()
    my_list.contains(81)
    my_list.insert(32, 0)
    my_list.display()
    my_list.insert(33, 44)
    my_list.display()
    my_list.insert(34, 3)
    my_list.display()
    my_list.remove(9)
    my_list.display()
    my_list.remove(33)
    my_list.display()
    my_list.remove(81)
    my_list.display()
    my_list.add(101)
    my_list.add(102)
    my_list.add(17)
    my_list.display()
    my_list.remove(17)
    my_list.insert(320, 320)
    my_list.contains(206)
    my_list.contains(32)
    my_list.contains(17)
    my_list.contains(101)
    my_list.contains(175)
    my_list.display()
    my_list.insert(3, 3)
    my_list.display()
    my_list.insert(127, 0)
    my_list.display()
    my_list.insert(129, 32)
    my_list.display()
    my_list.reverse()
    my_list.display()


if __name__ == '__main__':
    main()
"""