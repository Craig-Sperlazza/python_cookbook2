# project-8b
# Author: Craig Sperlazza
# Date: 2/19/2020
# Description: The program uses a decorator function that decorates functions to
# provides a runtime measurement capability of those functions.
# In this particular case, the decorator function will be used to compare the
# performance a bubble sort algorithm versus an insertion sort algorithm on
# randomly generated lists ranging in size from 1000 to 10,000 in
# 1000 integer increments. Ultimately, this program will provide a graph
#comparing the performance of the two algorithims.

from matplotlib import pyplot
import random
import time
import functools

def sort_timer(func):
    """decorator function that accepts a function as a parameter and
     returns the runtime of that function"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        initial_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time_elapsed = end_time - initial_time
        return total_time_elapsed
    return wrapper

#bubble_sort
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

#insertion_sort
@sort_timer
def insertion_sort(a_list):
  """
  :param accepts a list as a parameter
  :return does not return anything but does:
  Sort the parameter list in ascending order using the insertion sort
  """
  for index in range(1, len(a_list)):
    value = a_list[index]
    pos = index - 1
    while pos >= 0 and a_list[pos] > value:
      a_list[pos + 1] = a_list[pos]
      pos -= 1
    a_list[pos + 1] = value

def compare_sorts(func1, func2):
    """
    :param func1: bubble sort function decorated with sort_timer wrapper
    :param func2: insertion sort function decorated with sort_timer wrapper
    :return: This function will ultimately generate a graph comparing the
    sort speed for each of the two functions. It will perform this as follows:
    compare_sorts will generate a list of 1000 random numbers
    in the range 1 <= r <= 10000. It will then run each sorting function
    on that list of numbers and time each function's runtime. This will provide
    the first data point for the graph. This process will be repeated for
    2000 random numbers, then 3000 random numbers, etc., all the way up to 10000.
    """
    local_bubble_sort = func1
    local_insertion_sort = func2
    bub_lst = []
    ins_lst = []
    for i in range(1000, 11000, 1000):
        #calls the randon_int_generator function to generate a random list the
        #size of i during each iteration of the for loop
        bubble_list = random_int_generator(i)
        #print(len(bubble_list))
        insertion_list = list(bubble_list)
        #calls the bubble sort on its list to get the time
        bubble_time = local_bubble_sort(bubble_list)
        #calls the insertion sort on its list to get the time
        insertion_time = local_insertion_sort(insertion_list)
        #once we have the run time, each will be appended to their specific list
        #of runtimes.
        bub_lst.append(bubble_time)
        ins_lst.append(insertion_time)

    #print(len(bubble_list))
    #print(bubble_list)
    #print(bub_lst)
    #print(ins_lst)
    #print(bub_lst[0])
    #print(bub_lst[1])

    pyplot.plot([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
                [bub_lst[0], bub_lst[1], bub_lst[2], bub_lst[3], bub_lst[4], 
                bub_lst[5], bub_lst[6], bub_lst[7], bub_lst[8], bub_lst[9]], 'ro--', linewidth=2)
    pyplot.plot([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
                [ins_lst[0], ins_lst[1], ins_lst[2], ins_lst[3], ins_lst[4], 
                ins_lst[5], ins_lst[6], ins_lst[7], ins_lst[8], ins_lst[9]], 'go--', linewidth=2)
    pyplot.show()



def random_int_generator(total_int):
    """This function will be called by the compare_sorts function
    on each iteration throught its for loop and will generate a random list of
    integers the size of the total_int parameter passed to it
    via the compare sorts function.
    """
    start_int = 1
    end_int = 10000
    total_int = total_int
    random_int_list = []
    for j in range(total_int + 1):
        random_int_list.append(random.randint(start_int, end_int))
    return random_int_list

#print(random_int_generator(10000))

compare_sorts(bubble_sort, insertion_sort)