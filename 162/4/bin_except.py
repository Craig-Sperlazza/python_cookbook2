# project-4a
# Author: Craig Sperlazza
# Date: 1/16/2020
# Description: Program implements a  binary search function that
# raises a TargetNotFound exception when the target value is not in the list,
# but returns the index of the target value if it is in the list

from math import floor

class TargetNotFound(Exception):
    pass

def bin_except(a_list, target):
    """ Searches a_list for an occurrence of target
    If found, returns the index of its position in the list
    If not found, raises an error message indicating that
    the target value isn't in the list
    """
    first = 0
    last = len(a_list) - 1
    while first <= last:
        middle = floor((first + last) / 2)
        if a_list[middle] == target: #if the middle value is the target
            return middle
        if a_list[middle] > target: #if middle value is > target, go to small half
            last = middle - 1
        else: #else if middle value is < target, go to large half of list
            first = middle + 1
    raise TargetNotFound #exception is raised if target is not in the list


"""
list1 = [5,6,7,8,9]

print(bin_except(list1, 7))

list2 = [1,2,3,4,5]
print(bin_except(list2, 12))
"""