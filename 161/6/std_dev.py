"""
# project-6c
# Author: Craig Sperlazza
# Date: 10/31/2019
# Description: Creates a Person class that contains two data members,
name and age. Additionally, creates a separate function that calculates
the population standard deviation of the ages of Person Objects
"""

import math

class Person:
    """Creates a Person class that contains two data members, name and age."""
    def __init__(self, name, age):
        self.name = name
        self.age = age


def std_dev(person_list):
    """Calculates the population standard deviation. This separate function
     can be used to calculate the std dev of the ages of Person Objects"""
    mean_total = 0
    variance_total = 0

    # creates a new list of integer ages from the Person Objects
    age_list = [i.age for i in person_list]

    # standard deviation requires at least 2 numerical inputs
    if len(age_list) <= 1:
        return "False"

    # sums the integers from the age_list for use in finding the mean value
    for i in age_list:
        mean_total = mean_total + i


    mean = mean_total / len(age_list)

    # creates a new list containing variance, which is the squared difference of
    # the mean subtracted from each individual age in age_list
    variance = [(i - mean) ** 2 for i in age_list]

    # sums the integers from the variance list for use in finding the mean value
    for i in variance:
        variance_total = variance_total + i

    mean_variance = variance_total / len(variance)

    pop_std_dev = math.sqrt(mean_variance)

    return pop_std_dev






