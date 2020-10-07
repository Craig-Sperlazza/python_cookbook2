# project-7a
# Author: Craig Sperlazza
# Date: 10/31/2019
# Description: Creates a function that takes a list as a parameter
# and squares the values of the list (mutates original list)

def square_list(user_list):
    """Takes a list as a parameter and squares the values of the list"""
    for value in range(len(user_list)):
        user_list[value] = user_list[value] ** 2

"""
num_list = [8]
square_list(num_list)
print(num_list)

orig = [7, -3, 12, 9]
print(orig)
square_list(orig)
print(orig)

orig2 = [-10, 2.5, 0, 7]
print(orig2)
square_list(orig2)
print(orig2)
"""
