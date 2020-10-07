# CS 261 project-2-1
# Author: Craig Sperlazza
# Date: 4/05/2020
# Program Description:
#   student_list.py
#   Reimplementation of Pythons List
# ===================================================
# balance.py
# ===================================================
# Using a stack to check for unbalanced parentheses
# ===================================================

import sys

# Checks whether the input string is balanced
# param: input string
# returns True if string is balanced, otherwise returns False
def is_balanced(input_string):

    # initialize an empty list as the stack
    stack = []

    # iterate over each character in the string
    for i in input_string:
        if len(input_string) == 0:
            # print("0 length is balanced")
            # print("True")
            return True
        else:
            if i == "[" or i == "{" or i == "(":
                stack.append(i)

            if i == "]":
                if stack == []:
                    return False
                elif stack[-1] != "[":
                    # print("False, [")
                    return False
                elif stack[-1] == "[":
                    # print("balanced thus far []")
                    stack.pop()

            if i == "}":
                if stack == []:
                    return False
                elif stack[-1] != "{":
                    # print("False, }")
                    return False
                elif stack[-1] == "{":
                    # print("balanced thus far {}")
                    stack.pop()

            if i == ")":
                if stack == []:
                    return False
                elif stack[-1] != "(":
                    # print("False, ()")
                    return False
                elif stack[-1] == "(":
                    # print("balanced thus far ()")
                    stack.pop()
    if len(stack) != 0:
        return False
    else:
        return True


if __name__ == '__main__':
    # get input string
    _input_string = sys.argv[1]  # DO NOT MODIFY

    balanced = is_balanced(_input_string)

    if balanced:
        print("The string {} is balanced".format(_input_string))
    else:
        print("The string {} is not balanced".format(_input_string))