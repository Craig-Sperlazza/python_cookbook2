# CS 261 project-2-1
# Author: Craig Sperlazza
# Date: 4/05/2020
# Program Description:
#   student_list.py
#   Reimplementation of Pythons List
# ===================================================


import numpy as np

# StudentList class is our implementation of Python's List
class StudentList:
    def __init__(self):
        """creates an empty array of length 4, initialized for 16 bit integers"""
        self._list = np.empty([4], np.int16)
        self._capacity = 4
        self._size = 0

    def __str__(self):
        return str(self._list[:self._size])

    # You may want an internal function that handles resizing the array.
    # Dont modify get_list or get_capacity, they are for testing

    def get_list(self):
        return self._list[:self._size]

    def get_capacity(self):
        return self._capacity

    def get_size(self):
        """returns the size (i.e. number of elements) of the array"""
        return self._size

    def get_size_special(self):
        """Tried to use the built-in numpy function--DOES NOT WORK CURRENTLY"""
        return self._list.size

    def _upsize(self):
        """This doubles capacity of the numpy array and copies the old array
        This method is largely taken from Module 3 in CS 261"""
        new_data = np.empty([self._capacity * 2], np.int16)
        # must use a temporary list because it changes it in place.
        for index in range(self._size):
            # np.insert (array, index to insert, value to insert)
            temp_list = np.insert(new_data, index, self._list[index])
            new_data = temp_list
        self._capacity = self._capacity * 2
        return new_data

    def append(self, val):
        """
        :param val: takes the value you wish to append
        :return: Needs to check if there is room in the numpy array
         and call _upsize if there isn't, which in turn will double the size of
         the array and then append will append the value passed in"""
        if self._size == self._capacity:
            self._list = self._upsize()
        self._list[self._size] = val
        self._size = self._size + 1

    def pop(self):
        """
        One note of importance: This method must reduce the size parameter by 1
        to account for the fact that the list size will decrease by one
        :return: This method will remove the last item from the numpy array and
        return the value of that item
        This function was taken in large part from Module 7 in CS 162
        """
        val = self._list[self._size - 1]
        temp_list = np.delete(self._list, -1)
        self._size = self._size - 1
        self._list = temp_list
        return val

    def insert(self, index, val):
        """
        :param index: index in the list where you want to insert the value
        :param val: value you want to insert into the list
        :return: update self._list with the new value but does not return
        anything
        SPECIAL NOTE: Must check for capacity and double the capacity if full
        """
        if self._size == self._capacity:
            self._list = self._upsize()
        temp_list = np.insert(self._list, index, val)
        self._list = temp_list
        self._size = self._size + 1


    def remove(self, val):
        """
        :param val: takes the value you wish to remove
        :return: Does not return anything if the value is found but does
        remove the first instance of the value from the list.
        This method also reduces the size of the  list if the value is found.
        """
        count = 0
        for j in range(self._size):
            if count == 0 and self._list[j] == val:
                temp_list = np.delete(self._list, j)
                count = count + 1
        self._size = self._size - count
        if count >= 1:
            self._list = temp_list

    def clear(self):
        """the clear method clears the array by setting the array to a new
         array of size 4 integers"""
        new_data = np.empty([4], np.int16)
        self._list = new_data
        self._capacity = 4
        self._size = 0

    def count(self, val):
        count = 0
        for j in range(self._size):
            if self._list[j] == val:
                count = count + 1
        return count

    def get(self, index):
        """
        :param index: pass in the index of the value you would like to retrieve
        :return: returns the value at the requested index """
        return self._list[index]

"""
print("\nInitializing list")
my_list = StudentList()

print(my_list)

for i in range(17):
    my_list.append(i)
    print(my_list)
print(my_list)

print(my_list.pop())
print(my_list)

my_list.insert(3, 32)
print(my_list)

print(my_list.get(3))
my_list.remove(32)
print(my_list)
print(my_list.get_size())
print(my_list.get_list())
my_list.append(5)
my_list.append(5)
print(my_list.get_list())
print(my_list.count(5))
my_list.remove(5)
print(my_list.get_list())
print(my_list.count(5))
my_list.remove(5)
print(my_list.get_list())
print(my_list.count(10))
print(my_list.count(23))

my_list.clear()
print(my_list)
"""

