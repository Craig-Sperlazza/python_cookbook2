# project-6a
# Author: Craig Sperlazza
# Date: 2/04/2020
# Description: The program creates a recursive function named array_max that
# takes as a parameter a list of numbers and returns the max value in the list.

def array_max(int_lst):
    """
    :param int_lst: Takes as a parameter a list of integers (assumes at least
    one integer value in the list)
    :return: Perform a recursive algorithm to return the max integer value
    """
    if len(int_lst) == 1:
        #print(int_lst[0])
        return int_lst[0]
    elif len(int_lst) > 1:
        max_value = max(int_lst[0:]) #gets the max value of the list
        #print(max_value, "max")
        #print(int_lst[0], "0 index")
        if int_lst[0] >= max_value: #returns list[0] if == max value
            return int_lst[0]
        # if the list index is not max, slices it, continues recursively
        elif int_lst[0] < max_value:
            slice_int_lst = int_lst[1:]
            return array_max(slice_int_lst)


"""
################TESTING#########################################################
test_list_single = [2]
test_list = [62, 3, 15, 22, 8, 1, 34]
test_list2 = [-62, 3, 15, -22, 8, 1, 34, -16]
test_list3 = [3, 6, 8, 9, 12, 32, 22]
test_list4 = [2, 2, 2, 2, 2, 2,]
test_list5 = [0, 0, 0, 0, 0]
test_list6 = [0, 1, 2, 3, 4, 5, 6]
test_list7= [6, 5, 4, 3, 2, 1, 0]
test_list8 = [-1, -2, -3, -4, -5]
test_list9 = [-5, -4, -3, -2, -1, 0]
test_list10= [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
test_list11 = [-1, -2, 3, 3, 2]

#test_gradescope = [1, 3, 100, 2]


print(array_max(test_list_single), "one")
print(array_max(test_list2), "two")

print(array_max(test_list3), "three")
print(array_max(test_list4), "four")
print(array_max(test_list5), "five")
print(array_max(test_list6), "six")
print(array_max(test_list7), "seven")
print(array_max(test_list8), "eight")
print(array_max(test_list9), "nine")
print(array_max(test_list10), "ten")
print(array_max(test_list11), "eleven")

#print(array_max(test_gradescope), "grade")


array_max(test_list)
array_max(test_list2)
array_max(test_list3)
array_max(test_list4)
array_max(test_list5)
array_max(test_list6)
array_max(test_list7)
array_max(test_list8)
array_max(test_list9)
array_max(test_list10)
array_max(test_list11)
array_max(test_gradescope)


#print(max(test_list)) #returns the max number regardless of position
#print(max(test_list[1:])) # max function will work by slicing off first index
"""