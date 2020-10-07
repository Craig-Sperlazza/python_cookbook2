# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:16:55 2019

@author: Csperlazza
"""

def fibby(n):
    '''
    returns the nth number of the fibonacci sequence
    '''
    if n == 0:
        return 0
    if n  == 1:
        return 1
    return fibby(n - 1) + fibby(n-2)

print(fibby(2))