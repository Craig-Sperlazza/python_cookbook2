# project-4c

# Author: Craig Sperlazza
# Date: 10/13/2019
# Description: Hailstone function takes a positive integer as a parameter and returns the number of steps it takes to get from the integer to 1 by applying the Hailstone Sequence

def hailstone(num):
    """Takes a positive integer as a parameter and returns the number of steps it takes to get from the integer to 1 using the Hailstone Sequence"""
    count = 0 #The count variable is set to 0 outside of the main loop to make sure it does not reset
    if num == 1: #the number 1 is a special case where the hailstone sequence returns 0 so the function deals with the number 1 seperately.
        return(0)
    else:
        while num != 1: #The Hailstone Sequence reaching the value of 1 is our exit condition
            if num % 2 == 0:
                num = num // 2
                count += 1 #This updates the count variable each time the conditional is run
            else:
                num = (num * 3) + 1
                count += 1 #This updates the count variable each time the conditional is run
    return(count) #Set the return statement outside the loop so once the loop exits (or does not run in the special case) this will return the final value for the count variable

