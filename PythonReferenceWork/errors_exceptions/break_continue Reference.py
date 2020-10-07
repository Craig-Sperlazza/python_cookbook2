# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 11:34:37 2019

@author: Csperlazza
"""
"""
continue statement & readability
Module 3. Iteration (Looping)

 

break and continue

 
"""
#The "break" statement stops the execution of the loop.


for num in range(1, 11):    
  if (num == 5):        
    break    
  print(num)

#>>> 1, 2, 3, 4
 

#The "continue" statement jumps out of a conditional testing section and proceeds to the next iteration.

for num in range(1, 11):    
  if (num == 5):        
    continue
  print(num)

#>>> 1, 2, 3, 4, 6, 7, 8, 9, 10
 

#Both code snippets below produce the same result.

#Some people consider Example 2 to be more readable.

 

 

str_1 = "Waaaa1"
str_2 = "Oaaaa1"
str_3 = "N!aa1"

str_4 = "Waaaa0"
str_5 = "Oaaaa1"
str_6 = 'N!aaa1'

str_7 = "Waaaa1"
str_8 = "Oaaaa1"
str_9 = "N?aaa1"

str_10 = "Waaaa1"
str_11 = "Oaaaa1"
str_12 = "N!aaa1"


case_1 = [str_1, str_2, str_3]
case_2 = [str_4, str_5, str_6]
case_3 = [str_7, str_8, str_9]
case_4 = [str_10, str_11, str_12]

cases = [case_1, case_2, case_3, case_4]
 

#Example 1:

for case in cases:

    word = ''
    
    # case_1: False
    if len(case[2]) == 6:
        
        # case_2: False
        if case[0][5] + case[1][5] + case[2][5] == '111':
            
            # case_3: False 
            if '!' in case[2]:
                
                # case_4: Test
                for str in case:
                    word += str[0]
               
                print(word)
 

#Example 2:

for case in cases:
    
    word = ''
    
    # case_1: False
    if len(case[2]) != 6:
        continue
    
    # case_2: False
    if case[0][5] + case[1][5] + case[2][5] != '111':
        continue
    
    # case_3: False   
    if '!' in case[2]:
           
        # case_4: Test
        for str in case:
            word += str[0]
            
        print(word)
            