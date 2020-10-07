# project-1
# Author: Craig Sperlazza
# Date: 1/7/2020
# Description: Utilizes a Person class to create person objects containing a
# person's name and age. Also, uses a separate statistics function that makes
# use of the statistics library to compute mean, median, and mode ages

import statistics

class Person:
    """Person Class that has two data members: the persons name and age"""

    def __init__(self, name, age):
        """Initializes a person"""
        self.name = name
        self.age = age

def basic_stats(person_list):
    """Function that accepts a list made up of objects created in the Person
    Class and makes use of the statistics library to return the mean,
    median and mode of the ages"""

    age_list = [i.age for i in person_list] #makes a new list of only ages
    stats_tup = (statistics.mean(age_list), statistics.median(age_list),
                 statistics.mode(age_list))
    return(stats_tup)

"""
p1 = Person("Kyoungmin", 73)
p2 = Person("Mercedes", 24)
p3 = Person("Avanika", 48)
p4 = Person("Marta", 24)

person_list = [p1, p2, p3, p4]
print(basic_stats(person_list))

p5 = Person("Kyoungmin", 2)
p6 = Person("Mercedes", 4)
p7 = Person("Avanika", 6)
p8 = Person("Marta", 2)

person_list = [p5, p6, p7, p8]
print(basic_stats(person_list))
"""
