"""
You are given a puzzle consisting of a row of squares that contain non-negative integers,
with a zero in the rightmost square.

You have a token that starts on the leftmost square.

On each turn, the token can shift left or right a number of squares equal to the value in its current square,
but is not allowed to move off either end.

For example, if the row of squares contains these values: [2, 4, 5, 3, 1, 3, 1, 4, 0],
then on the first turn the only legal move is to shift right two squares, because the starting square contains a 2,
and the token can't move off the left end.

The goal is to get the token to the rightmost square (that contains zero).

This row has a solution (more than one), but not all rows do.

If we start with the row [1, 3, 2, 1, 3, 4, 0], then there is no way for the token to reach the zero.

Write a recursive function named row_puzzle that takes a list of integers as a parameter
and returns True if the puzzle is solvable for that row, but returns False otherwise.

You may use default arguments and/or helper functions.

The file must be named: row_puzzle.py

"""

def help_row_puzzle (user_lst, current_position, count):
    current_value = user_lst[current_position]
    lst_length = len(user_lst)
    print(user_lst, current_position, current_value, count)
    lst_length_squared = lst_length * lst_length
    low_int_value = user_lst[current_position - current_value]
    high_int_value = user_lst[current_position + current_value]

    if current_position + current_value == lst_length - 1 :#current_value == 0:
        return True
    else:
        if count > lst_length_squared:
            return False
        elif (current_position + current_value) <= (lst_length - 1): #and (current_position - current_value) >= 0:
            current_position = current_position + current_value
            count = count + 1
            return help_row_puzzle(user_lst, current_position, count)
        elif (current_position - current_value) >= 0: #and (current_position + current_value) <= (lst_length - 1):
            current_position = (current_position - current_value)
            count = count + 1
            return help_row_puzzle(user_lst, current_position, count)


def row_puzzle(user_lst):
    return help_row_puzzle(user_lst, 0, 0)


gs_lst1 = [2, 4, 5, 3, 1, 3, 1, 4, 0]
gs_lst2 = [1, 3, 2, 1, 3, 4, 0]
single = [0]
two = [1, 0]
three = [1, 2, 3, 1, 3, 1, 1, 0]

print(row_puzzle(gs_lst1))
print(row_puzzle(gs_lst2))
print(row_puzzle(single))
print(row_puzzle(two))
print(row_puzzle(three))