# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 22:10:42 2019

@author: Csperlazza
"""


sample_list9 = [1, 3, 5, 3.3, 7]



def find_median(num_list):
    sorted_list = sorted(num_list)
    print(sorted_list)
    length = len(sorted_list)
    if length <= 1: #This is a special case because by the definition of median: a list with n<=1 elements has no median
        return None
    elif length % 2 == 0:
        even_value_1 = sorted_list[(length // 2)-1]  #when getting the correct values from the list, the "-1" accounts for 0 indexing
        even_value_2 = sorted_list[length // 2]      #floor division ensures an integer value for list index(a list index may not be a float)
        even_median = (even_value_1 + even_value_2) / 2    #use regular division for the final number since some will be a float
        return even_median
    elif length % 2 != 0:
        odd_median = sorted_list[(length -1) // 2]
        return odd_median

print(find_median(sample_list9))