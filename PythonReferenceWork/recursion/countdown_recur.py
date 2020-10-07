# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 10:12:32 2019

@author: Csperlazza
"""

def countdown(num):
    """
    return a countdown string, for e.g. input 5, return "5 4 3 2 1"
    """
    if num == 1:
        return str(num)
    else:
        return str(num) + " " + countdown(num - 1)
print(countdown(5))

"""
def countdown(n):
  if n < 2:
    return str(n)
  return str(n)+" "+countdown(n-1)
"""