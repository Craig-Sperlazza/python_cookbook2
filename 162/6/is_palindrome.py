# project-6c
# Author: Craig Sperlazza
# Date: 2/04/2020
# Description: The program creates a recursive function named is_palindrome that
# takes a string parameter and returns True if that string is a palindrome,
# and False otherwise.

def is_palindrome(user_str):
    """
    :param usr_str: Takes as a parameter a string
    :return:
        Performs a recursive algorithm and returns True if:
            The string is a palindorme, which is a string that reads
            the same forwards and backwards. A palindrome can be a string size
            that is even, for e.g. "hannah" or odd, for e.g. "tacocat".
        Returns False if: The string is not a palindrome.  It is important to
        note that  this function does NOT ignore case punctuation.
        For example, "Tacocat" or "taco, cat" would return False.
    """
    # If string size equals 0 (initially or after slicing)- it is a palindrome
    # and True is returned
    if len(user_str) == 0:
        return True

    #If string size equals one (initially or after slicing)- it is a palindrome
    #and True is returned
    if len(user_str) == 1:
        return True

    # If string size equals two (initially or after slicing)- it is a palindrome
    # if the characters are the same and True is returned, False otherwise
    elif len(user_str) == 2:
        if user_str[0] == user_str[1]:
            return True
        else:
            return False
    else:
        if user_str[0] != user_str[-1]: #False: first and last letter not equal
            return False
        # else slices index [0] and [-1], continues recursively to compare the next two values
        else:
            slice_user_str = user_str[1:-1]
            return is_palindrome(slice_user_str)


"""
str0 = ""
str1 = "a"
str2 = "Hannah"
str3 = "hannah"
str4 = "hanna"
str5 = "Hanna"
str6 = "aa"
str7 = "Aa"
str8 = "tacocat"
str9 = "Tacocat"
str10 = "taco cat"
str11 = "racecar"


print(is_palindrome(str0))
print(is_palindrome(str1))
print(is_palindrome(str2))
print(is_palindrome(str3))
print(is_palindrome(str4))
print(is_palindrome(str5))
print(is_palindrome(str6))
print(is_palindrome(str7))
print(is_palindrome(str8))
print(is_palindrome(str9))
print(is_palindrome(str10))
print(is_palindrome(str11))
"""
