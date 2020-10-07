# project-4c
# Author: Craig Sperlazza
# Date: 1/16/2020
# Description: Program contains an insertion sort that takes as input a list
#   of strings and sorts them using the insertion sort method. The sorting
#   ignores case

def string_sort(str_list):
    """This function takes a list of strings and sorts them in
    ascending order. This function ignores case in its sorting by implementing
    the .casefold() method in the while comparison.
    For example, apple == Apple and apple will be sorted before Zebra.
    This implementation of the insertion sort algorithm is based on the
    textbook suggested by Professor Alcon: Problem Solving With Algorithms
    by Bradley Miller page 215. It has been modified to sort strings,
    to ignore case using the .casefold() method, to sort ascending,
    and to adhere to our best practices regarding naming conventions"""
    for index in range(1, len(str_list)):
        value = str_list[index]
        #print(value)
        position = index

        while position > 0 and str_list[position - 1].casefold() > value.casefold():
            str_list[position] = str_list[position - 1]
            position = position - 1
        str_list[position] = value

"""
######################TESTING SORT FUNCTION STRING_SORT#########################

test_list = ["marble", "Zebra", "apple", "maRker", "candy", "BALL", "TEMporarY"]

list_2 = ["ZEBRA", "XYZ", "Monty", "cup", "BaskET", "age","AGED", "Zip"]

string_sort(test_list)

print(test_list)

string_sort(list_2)

print(list_2)
"""
"""
############Testing casefold()##################################
string1 = "apples"
string2 = "Apples"

# Expected result Apples = to apples
if string1.casefold() == string2.casefold():
    print("strings are equal.")
else:
    print("strings are not equal.")


str1 = "apple"
str2 = "Zebra"

print(ord("A")) #65
print(ord("a")) #97
print(ord("z")) #122

if str1.casefold() > str2.casefold(): #if no casefold() apple should be greater
    print("apple is greater")
else:
    print("Zebra is greater")
"""
