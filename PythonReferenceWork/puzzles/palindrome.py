# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:20:20 2019

@author: Csperlazza

"""

def is_pal(user_str):
  if len(user_str) <= 1:
    return False
  else:
    for i in range(0, len(user_str)//2):
      if user_str[i] != user_str[len(user_str)-i-1]:
        return False
      else:
        return True
  
def is_pal(s):
  return s[::-1] == s