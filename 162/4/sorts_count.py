# project-4d
# Author: Craig Sperlazza
# Date: 1/16/2020
# Description: This program has two functions. A bubble sort function and
#    and insertion sort function that both count the
#    number of comparisons and the number of exchanges made while sorting a list
#    and returns a tuple of the two values (comparisons first, exchanges second)


def bubble_count(a_list) -> tuple:
    """This function implements a bubble sort algorithm to sort a user's input.
    It will sort the input in ascending order.
    As it sorts the data, it computes a count of the number of comparisons
    and the number of exchanges the algorithm makes during its sorting.
    The function then returns a tuple with (comparisons, exchanges)."""
    compare_count = 0  # Tracks number of comparisons the algorithm makes
    exchange_count = 0  # Tracks number of exchanges the algorithm makes

    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp
                exchange_count = exchange_count + 1
                #exhange counts each time if conditional is triggered
            compare_count = compare_count + 1
            #compare count must be outside so it counts when if is true or false
    compare_exchange_tup = (compare_count, exchange_count)
    #print(compare_exchange_tup)
    return compare_exchange_tup


def insertion_count(a_list) -> tuple:
    """This function implements an insertion sort algorithm to sort user input.
    It will sort the input in ascending order.
    As it sorts the data, the function computes a count of the number of
    comparisons and the number of exchanges the algorithm makes during sorting.
    The function then returns a tuple with (comparisons, exchanges)."""

    compare_count = 0  # Tracks number of comparisons the algorithm makes
    exchange_count = 0  # Tracks number of exchanges the algorithm makes

    for index in range(1, len(a_list)):
        value = a_list[index]
        position = index
        compare_count = compare_count + 1 #Counts compares as you enter loop
        while (position - 1) >= 0 and a_list[position - 1] > value:
            if (position - 1) == 0:
                # This eliminates too many comparisons (i.e. overcounting)
                # by taking into account values in front of list that are sorted
                compare_count = compare_count - 1
            a_list[position] = a_list[position - 1]
            position = position - 1
            compare_count = compare_count + 1 #counts compare w/ actual exchange
            exchange_count = exchange_count + 1
        a_list[position] = value
    #print(compare_count)
    compare_exchange_tup = (compare_count, exchange_count)
    #print(compare_exchange_tup)
    return compare_exchange_tup

"""
####################TESTING####################################################

piazza_list1 = [1,3,5,2,4]
piazza_list2 = [1,3,5,2,4]

#bubble_count(piazza_list1)
#print(piazza_list1)

insertion_count(piazza_list2)
print(piazza_list2)


gradescope_list1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
gradescope_list2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#bubble_count(gradescope_list1)
#print(gradescope_list1)

insertion_count(gradescope_list2)
print(gradescope_list2)

done_list = [0, 1, 2, 3, 4, 5]

#bubble_count(done_list)
#print(done_list)

insertion_count(done_list)
print(done_list)

random_list = [ 3, 66, 2, 7, 9]
#bubble_count(random_list)
#print(randome_list)

insertion_count(random_list)
print(random_list)

"""