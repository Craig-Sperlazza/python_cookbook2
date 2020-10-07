# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 09:53:45 2019

@author: Csperlazza

Here the base case is when the sequence arrives at 1. 
You can see that there are two different recursive cases - 
one that happens if num is odd, and one that happens if num is even. 

We add 1 to the return value, since the current copy of hailstone takes 
one more step to reach 1 than the recursive call does. 
For example, if we start at 3, the sequence goes: 3, 10, 5, 16, 8, 4, 2, 1. 
If we find the number of steps it takes to go from 10 to 1, 
then we can just add 1 more step to get the number of steps it takes to go from 3 to 1.
"""

def hailstone(num):    
  """    
  Returns the number of steps it takes for a hailstone sequence that starts
  at num to reach 1    
  """    
  if num == 1:        
    return 0    
  if num % 2 == 0:  # if num is even        
    return hailstone(num/2) + 1    
  else:       
    return hailstone(num*3+1) + 1
print(hailstone(3))