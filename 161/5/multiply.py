# project-5a

# Author: Craig Sperlazza
# Date: 10/22/2019
# Description: Function that takes two integers as parameters and arrives at the
# product of the two integers by recursively summing together parameter a by
# parameter b times


def multiply(num1, num2):
    """ Multiply function takes two parameters and finds their product through
     recursively calling the function"""
    if num2 == 0: #basecase: multiply does not call itself once num2 == 0
        return num2
    return num1 + multiply(num1, num2 - 1)





