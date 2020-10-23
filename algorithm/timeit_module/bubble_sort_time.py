# from matplotlib import pyplot
import random
import time
import functools

def sort_timer(func):
    """decorator function that accepts a function as a parameter and
     returns the runtime of that function"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        initial_time = time.perf_counter()
        # result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time_elapsed = end_time - initial_time
        # return total_time_elapsed
        return func(*args, **kwargs), total_time_elapsed
    return wrapper

#bubble_sort---once you wrapp it it only returns time
@sort_timer
def bubble_sort(a_list):
    """
    :param accepts a list of integers as a parameter
    :return does not return anything but does:
    Sort the parameter list in ascending order using the bubble sort algorithm
    """
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp
    return a_list

def make_rand_list(nums):
    random_list = []
    for i in range(0, nums):
        n = random.randint(1, 250)
        random_list.append(n)
    return random_list


if __name__ == '__main__':
    list1 = make_rand_list(100)
    list2 = make_rand_list(1000)
    list3 = make_rand_list(10000)
    # list4 = make_rand_list(25000)
    # list5 = make_rand_list(50000)
    # list6 = make_rand_list(100000)
    bubble_list = []
    
    bubble_list.append(bubble_sort(list1))
    bubble_list.append(bubble_sort(list2))
    bubble_list.append(bubble_sort(list3))
    # bubble_list.append(bubble_sort(list4))
    # bubble_list.append(bubble_sort(list5))
    # bubble_list.append(bubble_sort(list6))

    print(bubble_list)

    # print(list1)
    # print(list1)
    # print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
    # print(bubble_sort(list1))
