import numpy as np

class Dynamic_Array:
    def __init__(self):
        # creates an empty array of length 4, change the [4] to another value to make an
        # array of different length.
        self._list = np.empty([4], np.int16)
        self._capacity = 4
        self._size = 0

    def __str__(self):
        return str(self._list[:self._size])

    def _upsize(self):
        """This doubles capacity of the numpy array and copy over the old array.
        This method is largely taken from Module 3 in CS 261"""
        new_data = np.empty([self._capacity * 2], np.int16)
        #must use a temporary list because it changes it in place.
        for index in range(self._size):
            #np.insert (array, index to insert, value to insert)
            temp_list = np.insert(new_data, index, self._list[index])
            new_data = temp_list
        self._capacity = self._capacity * 2
        return new_data

    def append(self, val):
        # Needs to check if there is room and call _upsize if there isn't
        if self._size == self._capacity:
            self._list = self._upsize()

        self._list[self._size] =  val
        self._size = self._size + 1

my_list = Dynamic_Array()

# To begin with this will throw an index out of bounds error until you properly handle the capacity
# doubling.
for i in range(17):
    my_list.append(i)
    print(my_list)
print(my_list)