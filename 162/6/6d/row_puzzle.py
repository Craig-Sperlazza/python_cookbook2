# project-6d
# Author: Craig Sperlazza
# Date: 2/04/2020
# Program Description:
#   The program creates a recursive function named row_puzzle that
#   that takes a list of integers as a parameter and returns True if the puzzle
#   is solvable for that row, but returns False otherwise.

def help_row_puzzle(user_lst, current_position, count, new_count):
    """
    :param user_lst: User will provide a list of integers
    :param current_position: Default parameter: a starting position for each
        iteration. Initially set to position and updated according to the
        rules of gameplay (i.e. the next valid position)
    :param count: Default parameter: the amount of times the function has been
        recursively called. Allows management of maximum recursive depth.
    :param new_count: Default parameter: manages the interaction between
        increasing the starting position or decreasing the starting position if
        both options are available. The program will default to decrease until
        max count depth is reached and then switch to decreasing the position.
    :return: The function will return True if the
        puzzle is solvable for that row, but returns False otherwise.
    """

    current_value = user_lst[current_position] #value of the current position
    lst_length = len(user_lst)
    #below is just a test print function to print out loop counts and values
    #print(user_lst, current_position, current_value, count, new_count)
    lst_length_squared = lst_length * lst_length #max recursive depth

    if current_position + current_value == lst_length - 1: #game solved
        return True
    else:
        if count > lst_length_squared: #terminate game: max recursive depth
            return False

        elif (current_position + current_value) <= (lst_length - 1) and (current_position - current_value) >= 0:
            #statement accounts for both a legal increase and decrease move
            #new_count = 0
            #low_int_value = user_lst[current_position - current_value]
            #high_int_value = user_lst[current_position + current_value]

            # if/else: tries to increase and switches to decrease if limit reached
            if new_count < lst_length:
                count = count + 1
                new_count = new_count + 1
                high_int_value = current_position + current_value
                return help_row_puzzle(user_lst, high_int_value, count, new_count)
            else:
                count = count + 1
                new_count = new_count + 2
                low_int_value = current_position - current_value
                return help_row_puzzle(user_lst, low_int_value, count, new_count)

        #if increase is legal, try first
        elif (current_position + current_value) <= (lst_length - 1):
            current_position = current_position + current_value
            count = count + 1
            return help_row_puzzle(user_lst, current_position, count, new_count)

        #increase is illegal, so this tries to decrease position if legal
        elif (current_position - current_value) >= 0:
            current_position = (current_position - current_value)
            count = count + 1
            return help_row_puzzle(user_lst, current_position, count, new_count)


def row_puzzle(user_lst):
    """
    :param user_lst: User will provide a list of integers
    :return: The function will return, through a helper function True if the
    puzzle is solvable for that row, but returns False otherwise.

    Helper Function: The helper function named help_row_puzzle allows three
    default parameters to be passed to the game without user interaction.
    Specifically, the three parameters are a starting position for each iteration,
    a count (i.e. the amount of times the function has been recursively called),
    and a second count function that manages the interaction between increasing
    the starting position or decreasing the starting position if both options
    are available.

    Game Description:
    You are given a puzzle consisting of a row of squares that contain
    non-negative integers, with a zero in the rightmost square.
    You have a token that starts on the leftmost square. On each turn, the token
    can shift left or right a number of squares equal to the value in its current
    square, but is not allowed to move off either end.
    """
    return help_row_puzzle(user_lst, 0, 0, 0)





"""
####################    TESTING    #############################################
gs_lst1 = [2, 4, 5, 3, 1, 3, 1, 4, 0]
gs_lst2 = [1, 3, 2, 1, 3, 4, 0]
single = [0]
two = [1, 0]
three = [1, 2, 3, 1, 3, 1, 1, 0] #failing, should be true


print(row_puzzle(gs_lst1))
print(row_puzzle(gs_lst2))
print(row_puzzle(single))
print(row_puzzle(two))

print(row_puzzle(three))
"""





