# project-7b
# Author: Craig Sperlazza
# Date: 10/31/2019
# Description: Function that accepts a list as a parameter and
# reverses the order of the values of the list (mutates original list)

def reverse_list(user_list):
    """Accepts a list as a parameter and reverses the order of the
     values of the original list"""
    user_list[0:] = user_list[::-1]

"""
list1 = [7, -3, 12, 9]
print(list1)
reverse_list(list1)
print(list1)

list2 = [5, "craig", "stuck", 7, [1,2]]
print(list2)
reverse_list(list2)
print(list2)
"""
