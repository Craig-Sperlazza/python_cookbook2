# project-6b
# Author: Craig Sperlazza
# Date: 2/04/2020
# Description: The program creates a recursive function named is_decreasing that
# takes as its parameter a list of numbers and returns True if the elements of
# the list are strictly decreasing (each element in the array is strictly less
# than the previous one), and returns False otherwise.

def is_decreasing(int_lst):
    """
    :param int_lst: Takes as a parameter a list of integers (assumes at least
        two integer values in the list)
    :return: Perform a recursive algorithm to return True if:
        the elements in the list are strictly decreasing (that is each element
        in the array is strictly less than the previous one)
        Else: The algorithm will return False if any integer is not strictly
        decreasing (that is the subsequent integer is equal to or greater than
        the previous integer)
    """
    #If list size == two (initially or after slicing)-if statement compares
    #position [0] versus position [1]
    if len(int_lst) == 2:
        if int_lst[0] > int_lst[1]:
            #print(True)
            return True
        else:
            #print(False)
            return False
    elif len(int_lst) > 2:
        #anytime the 0 index is greater than 1 index, returns False and exits
        if int_lst[0] <= int_lst[1]: #returns False list[0] <= list[1]
            return False
        # if the list[0] > [1], the else is triggered which:
        # slices index [0], continues recursively to compare the next two values
        else:
            slice_int_lst = int_lst[1:]
            return is_decreasing(slice_int_lst)



"""
test_list1 = [62, 3, 15, 22, 8, 1, 34] #False
test_list2 = [-62, -22, -16] #False
test_list3 = [22, 15, 12, 6] #True
test_list4 = [2, 2, 2, 2, 2, 2,] #False
test_list5 = [0, 0, 0, 0, 0] #False
test_list6 = [0, 1, 2, 3, 4, 5, 6] #false
test_list7= [6, 5, 4, 3, 2, 1, 0] #true
test_list8 = [-1, -2, -3, -4, -5] #true
test_list9 = [-5, -4, -3, -2, -1, 0] #false
test_list10= [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5] #false
test_list11= [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5] #true
test_list12 = [-1, -2, 3, 3, 2]  #false
test_gradescope = [1, 3, 100, 2] #false


print(is_decreasing(test_list1), "one")
print(is_decreasing(test_list2), "two")
print(is_decreasing(test_list3), "three")
print(is_decreasing(test_list4), "four")
print(is_decreasing(test_list5), "five")
print(is_decreasing(test_list6), "six")
print(is_decreasing(test_list7), "seven")
print(is_decreasing(test_list8), "eight")
print(is_decreasing(test_list9), "nine")
print(is_decreasing(test_list10), "ten")
print(is_decreasing(test_list11), "eleven")
print(is_decreasing(test_list12), "twelve")
print(is_decreasing(test_gradescope), "grade")
"""

"""
##############    TESTING 2 VALUES-----ALL PASS###############
test_list_doubleTrue1 = [2, 1]
test_list_doubleTrue2 = [1, 0]
test_list_doubleTrue3 = [0, -1]
test_list_doubleTrue4 = [-1, -2]

test_list_doubleFalse1 = [1, 2]
test_list_doubleFalse2 = [0, 1]
test_list_doubleFalse3 = [-1, 0]
test_list_doubleFalse4 = [-2, -1]
test_list_doubleFalse5 = [-2, -2]
test_list_doubleFalse6 = [0, 0]
test_list_doubleFalse7 = [3, 3]

print(is_decreasing(test_list_doubleTrue1))
print(is_decreasing(test_list_doubleTrue2))
print(is_decreasing(test_list_doubleTrue3))
print(is_decreasing(test_list_doubleTrue4))

print(is_decreasing(test_list_doubleFalse1))
print(is_decreasing(test_list_doubleFalse2))
print(is_decreasing(test_list_doubleFalse3))
print(is_decreasing(test_list_doubleFalse4))
print(is_decreasing(test_list_doubleFalse5))
print(is_decreasing(test_list_doubleFalse6))
print(is_decreasing(test_list_doubleFalse7))
"""