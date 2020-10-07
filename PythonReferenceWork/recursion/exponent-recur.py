# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:03:52 2019

@author: Csperlazza
"""

def power(num, exp):
    """takes two numbers and multplies the first number by itself the second number of times"""
    if exp == 1: #exponent 1 is base case
        return num
    return num * pow(num, exp - 1) 

print(power(3, 4))