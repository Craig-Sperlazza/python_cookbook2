# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 10:15:57 2019

@author: Csperlazza

Write a recursive function called countup that takes a positive integer parameter 
and returns a string that counts up from 1 to that number.  
 For example, if 5 is passed to the function, it should return the string "1 2 3 4 5".  
You can use string concatenation in your recursive function to build up the return value.
"""

def countup(num):
    """Counts up from 1 to a selected number"""
  if num == 1:
    return str(num)
  else:
    return countup(num-1) + " " + str(num)
print(countup(5))

"""
def countup(n):
  if n < 2:
    return str(n)
    
  return countup(n-1)+" "+str(n)
"""