"""
# project-6a

# Author: Craig Sperlazza
# Date: 10/24/2019
# Description: Function that will take a list of numbers as a parameter and then
#sort the list values and then find the median value of the list values
"""

def find_median(num_list):
    """Takes a list of numbers (integers or floats) and returns the median"""
    num_list.sort()
    sorted_list = num_list
    length = len(sorted_list)

    # This is a special case because by the definition of median,
    # a list with n<=1 elements has no median
    if length <= 1:
        return None
    elif length % 2 == 0:
        # when getting values from the list, the "-1" accounts for 0 indexing
        # floor division ensures an integer value for list index
        even_value_1 = sorted_list[(length // 2)-1]
        even_value_2 = sorted_list[length // 2]
        # use regular division for the final number since some will be a float
        even_median = (even_value_1 + even_value_2) / 2
        return even_median
    elif length % 2 != 0:
        odd_median = sorted_list[(length - 1) // 2]
        return odd_median


