import numpy as np

"""
class BaseCollection(object):
    """Base class for everything. This code is taken from Module 3 lectures and
    in turn cites that "much of this code is taken from
    https://opendatastructures.org/" """

    def __init__(self):
        super(BaseCollection, self).__init__()

    def size(self):
        """This implementation works for almost every class in ODS"""
        return self.n

    def __len__(self):
        return self.size()

    def __str__(self):
        return "[" + ",".join(str(x) for x in self) + "]"

    def __repr__(self):
        return self.__class__.__name__ \
               + "([" + ",".join(repr(x) for x in self) + "])"


class StudentList(BaseCollection):
    def __init__(self):
        super(StudentList, self).__init__()
        # Create an empty Numpy array that will be the data structure for list
        self.__l = np.empty([4], np.int16)

    #def np.ndarray.__str__(self):

    # def __iter__(self):
    #     for i in range(len(self)):
    #         yield (self.__get(i))

    def __get(self, i):
        return self.__l[i]

    def get_array(self):
        return self.__str__()

    def append(self, item):
        np.append(self.__l, item)

    def insert(self, index, item):
        np.append(self.__l, index, item)

    def pop(self):
        last = self.__l[-1]
        self.__l = self.__l[:-1]
        #np.delete(self.__l, self.__l-1, item)
        return last

    def size(self):
        return self.__l.size

print("\nInitilizing list")
my_list = StudentList()
print(f"The list contains {my_list.get_array()}.")

# print("\nAdding a 1 and a 4")
# my_list.add(1)
# my_list.add(4)
# print(f"The list contains {my_list.get_array()}.")

You will only need to reimplement the following functions:

append(x)
pop() (only the last element)
insert (i, x)
remove (x)
clear ()
count (x)
get(i) - This should return the element found at index i.
Together append and pop can be used to represent a stack which will be needed in part 3.

In addition to having the above, correctly functioning operations the following requirements also apply:

The underlying array must begin with space allocated for 4 integers using Numpys array (Links to an external site.).
When an insert is attempted but there is not room for the insertion in the array it should double in size.
It must have a function get_array which returns the underlying Numpy array. This will facilitate testing and grading.
