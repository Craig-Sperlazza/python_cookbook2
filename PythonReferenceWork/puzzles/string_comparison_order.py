# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 09:47:32 2019

@author: Csperlazza
"""

def sort_two_strings(str1, str2):
  new_str1 = str1.lower()
  new_str2 = str2.lower()
  if new_str1[0] < new_str2[0]:
    str3 = str1 + " " + str2
    return str3
  else:
    str3 = str2 + " " + str1
    return str3