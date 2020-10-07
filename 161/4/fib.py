# project-4b

# Author: Craig Sperlazza
# Date: 10/13/2019
# Description: Takes an integer input from the user and returns the corresponding number of the fibonacci sequence

def fib(integer_position):
    """takes an integer and returns the corresponding Fibonacci sequence value"""
    first_fib = 0 # sets first_fib to 0 and second_fib to 1. This will allow them to be added to get the second Fibonacci value(which is 1)
    second_fib = 1
    if integer_position == 1: #The first integer is dealt with seperately from the rest of the sequence as a special case. This made the adding of the two placeholder variables feasible.
        return(1)
    else:
        for i in range(2, integer_position + 1): #Becasue the first Fibonacci value was treated as a special case, the starting range is adjusted so that the value of the iteration variable properly aligns with index of the Fibonacci sequence
            current_fib = first_fib + second_fib #The initial value is set to the second value of the fib sequence (1+0=1)
            first_fib = second_fib #Once the current_fib value is set in the prior step, the first_fib and second_fib are updated with the current second_fib and current_fib, thereby shifitng each value to the next number in the Fibonacci sequence
            second_fib = current_fib

            if i == integer_position:
                return(current_fib)



