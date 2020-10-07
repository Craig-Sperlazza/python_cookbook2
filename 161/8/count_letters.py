# project-8a
# Author: Craig Sperlazza
# Date: 11/7/2019
# Description:  Creates a function named count_letters that takes a string as a
# parameter a string and returns a dictionary that tabulates how many of each
# letter is in that string.

def count_letters(user_str):
    """Takes only the letters of a string and returns a dictionary with
     key:value pairs representing the letter (key) and its frequency(value)"""
    letter_count = {}
    #Alphabet list is used to filter out any non-alphabet characters
    alpha_lst = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"
,"Q","R","S","T","U","V","W","X","Y","Z"]

    upper_str = user_str.upper() #All characters uppercase(avoids duplication)

    if len(upper_str) == 0: #accounts for empty strings
        return letter_count
    else:
        for i in upper_str:
            for k in alpha_lst:
                #Adds a key:value pair to dict if not in dict (start value = 1)
                if i == k and i not in letter_count:
                    letter_count[i] = 1
                #Increments the value of key:value pair if pair already in dict
                else:
                    if i == k and i in letter_count:
                        letter_count[i] = letter_count[i] + 1
    return letter_count







