# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 09:41:34 2019

@author: Csperlazza

The base case is when b evenly divides a, 
in which case b is the greatest common divisor. 

Otherwise we make a recursive call with the value of b passed for a, 
and the value of a % b passed for b. 

Nothing needs to be done with the return values on the way back out of the recursive calls.
"""

def gcd(a, b):    
  """    
  Returns the greatest common divisor of a and b    
  """    
  if a % b == 0:        
    return b   
  
  return gcd(b, a % b)

print(gcd(100, 22))