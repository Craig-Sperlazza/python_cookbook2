"""
1. Define an exception named OutOfRangeError.  Write a function named numberName that asks the user for an integer,
    and if it's equal to 1, prints "one"; if it's equal to 2, prints "two", and if it's equal to 3, prints "three".  ' \
    'If the the parameter is not one of those three values, the function should raise an OutOfRangeError.  ' \
    'Write code that calls numberName in a try block, and handles the possible OutOfRangeError in an except block.
    It should handle an OutOfRangeError by printing "That's not one of the allowed values!"
"""
class OutOfRangeError(Exception):
    pass

def numberName():
    user_int = int(input("Please enter an integer"))
    if user_int == 1:
        print("one")
    elif user_int == 2:
        print("two")
    elif user_int == 3:
        print("three")
    else:
        raise OutOfRangeError

try:
    numberName()
except OutOfRangeError:
    print("That's not one of the allowed values!")
#else:
    #print(numberName())


