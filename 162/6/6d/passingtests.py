def help_row_puzzle(user_lst, current_position, count, new_count):
    current_value = user_lst[current_position]
    lst_length = len(user_lst)
    print(user_lst, current_position, current_value, count, new_count)
    lst_length_squared = lst_length * lst_length

    if current_position + current_value == lst_length - 1: #current_value == 0:
        return True
    else:
        if count > lst_length_squared:
            return False

        elif (current_position + current_value) <= (lst_length - 1) and (current_position - current_value) >= 0:
            #new_count = 0
            #low_int_value = user_lst[current_position - current_value]
            #high_int_value = user_lst[current_position + current_value]

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

        elif (current_position + current_value) <= (lst_length - 1): #and (current_position - current_value) >= 0:
            current_position = current_position + current_value
            count = count + 1
            return help_row_puzzle(user_lst, current_position, count, new_count)

        elif (current_position - current_value) >= 0: #and (current_position + current_value) <= (lst_length - 1):
            current_position = (current_position - current_value)
            count = count + 1
            return help_row_puzzle(user_lst, current_position, count, new_count)


def row_puzzle(user_lst):
    return help_row_puzzle(user_lst, 0, 0, 0)


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


