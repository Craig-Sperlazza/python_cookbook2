# project-8a
# Author: Craig Sperlazza
# Date: 2/19/2020
# Description: The program contains a generator function names count_seq that
# takes no parameters but will keep iterating indefinitely giving the following
# sequence: 2, 12, 1112, 3112, 132112, 1113122112, ... This sequence is defined
# as each number in the sequence being an enumeration of how many there are of
# each digit (in a row) in the previous number.


def count_seq():
    """
    :param: None
    :return: count_seq will keep iterating indefinitely giving the following
    sequence: 2, 12, 1112, 3112, 132112, 1113122112, ... This sequence is defined
    as each number in the sequence being an enumeration of how many there are of
    each digit (in a row) in the previous number
    """
    num = 1
    base = [1, 1, 1, 2]
    final_lst = []
    skip = False
    while True:
        if num == 1:
            yield 2
            num = 2
            #print(2)
        elif num == 2:
            yield 12
            num = 3
            #print(12)
        elif num == 3:
            #print(1112)
            yield 1112
            num = 4
        else:
            count = 0
            for i in range(4, num + 1): #this section selects the appropiate list
                if num == 4:
                    result = base
                else:
                    result = final_lst
                result_length = len(result)
                final_lst = []

                for i in range(1, result_length):
                    #print(final_lst)
                    if result[i] == result[i-1] and count == 0: # current value == previous value
                        count = count + 1

                    elif result[i] != result[i-1] and count == 1: #current value and previous value are not equal
                        #if count == 1: #count 1 means two duplicates
                        final_lst.append(2)
                        final_lst.append(result[i - 1])
                        if i == result_length - 1: #end of list
                            final_lst.append(1)
                            final_lst.append(2)
                            count = 0
                        count = 0

                    elif result[i] == result[i-1] and count == 1: #current value and previous value are not equal
                        count += 1

                    elif result[i] != result[i-1] and count == 2: #means the last two values are same as current
                        #print(count, "count2")
                        final_lst.append(3)
                        final_lst.append(result[i-1])
                        count = 0
                        if i == result_length - 1: #end of list
                            final_lst.append(1)
                            final_lst.append(2)

                    elif result[i] != result[i-1] and count == 0:
                        if i == result_length - 1: #end of list
                            final_lst.append(1)
                            final_lst.append(2)
                        else:
                            #print(final_lst)
                            final_lst.append(1)
                            final_lst.append(result[i-1])
                            #print(final_lst)
            #print(final_lst)
            #print(final_lst[-2])
            #print(len(final_lst), "R")
            base = final_lst
            str_lst = [str(item) for item in final_lst]
            #print(str_lst)
            yield_str = "".join(str_lst)
            yield(int(yield_str))

generator = count_seq()

"""
for i in range(8):
    print(next(generator))
"""


