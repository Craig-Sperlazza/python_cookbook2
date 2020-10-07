"""
# project-6b
# Author: Craig Sperlazza
# Date: 10/24/2019
# Description: Function that takes a list of first names as a parameter
# and returns a new list of first names that begin with "K" together with a
# last name, "Kardashian", added to each
"""

def add_surname(names_list):
    """Takes a list of first names as a parameter and returns a new list of
    first names that begin with "K" with "Kardashian" added to each"""
    kardashian_list = [i + " Kardashian" for i in names_list if i[0] == "K"]
    return kardashian_list

