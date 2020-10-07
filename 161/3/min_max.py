# project-3a

# Author: Craig Sperlazza
# Date: 10/7/2019
# Description: Asks the user to enter an integer (may assume that input is >= 1) to represent how many integers they want to enter and then returns a min and a max value for their integers.


user_num = int(input("How many integers would you like to enter?"))  # The user will enter her desired integer, which will then be used below in the for loop to set the number of iterations

max_value = 0  # maximum and minimum values will be initially set to 0, updated during the first iteration below, and then compared with each new inputed integer
min_value = 0

print("Please enter", user_num, "integers.")

for i in range(0, user_num):
    user_value = int(input()) #This will propmt the user to enter x amount of integers where x is equal to the variable user_num.

    if max_value == 0 and i == 0: #the initial max value is set to zero. In the first If statement, the condition will always be True, if and only if, it is the first (i.e. i == 0) iteration of the for loop.
        max_value = user_value

    elif max_value < user_value: #after the first iteration, this Elif statement will compare the max value and the current user value and update the max value if it is > the current user value
        max_value = user_value

    if min_value == 0 and i == 0: #The logic behind the min values works the same as the max described above.
        min_value = user_value

    elif min_value > user_value:
        min_value = user_value

print("min:", min_value)
print("max:", max_value)

