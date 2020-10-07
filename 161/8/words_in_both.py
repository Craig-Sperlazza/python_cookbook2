# project-8b
# Author: Craig Sperlazza
# Date: 11/7/2019
# Description: Creates a function named words_in_both that takes two strings
# as parameters and returns a set of the words contained in both strings


def words_in_both(str1, str2):
    """takes two strings as parameters and returns a set of the words
    contained in both strings"""

    # Transform all the string characters to lowercase to enable a proper
    # comparison of each string
    lower_case_str1 = str1.lower()
    lower_case_str2 = str2.lower()

    # Use split() function to split each string into a list of strings
    # Split on occurrences of whitespace.
    list1 = lower_case_str1.split()
    list2 = lower_case_str2.split()

    # Compare the items in  list1 and list 2 and then
    # add items in common to both lists to a new, empty list
    combined_list = []
    for i in list1:
        for k in list2:
            if i == k:
                combined_list.append(i)

    #Convert list to a set which will eliminate duplicates
    combined_set = set(combined_list)
    return combined_set
