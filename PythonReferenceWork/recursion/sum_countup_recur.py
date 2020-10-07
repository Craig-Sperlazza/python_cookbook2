# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 10:22:24 2019

@author: Csperlazza

 Write a recursive function called sum_countup that takes an integer parameter 
 and returns the sum of all the integers from 1 to that number.  
 
 For example if the function is passed the value 5, 
 then it should return 15 because 1 + 2 + 3 + 4 + 5 = 15.
"""

def sum_countup(num):
  if num == 1:
    return num
  else:
    return num + sum_countup(num-1)

"""
def sum_countup(n):
  if n == 1:
    return 1
    
  return n + sum_countup(n-1)

"""