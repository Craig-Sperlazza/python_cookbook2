# project-3b

# Author: Craig Sperlazza
# Date: 10/8/2019
# Description: Asks the user to enter and integer and then returns all factors (except 1 and itself)

user_int = int(input("Please enter a positive integer:"))

print("The factors of", user_int, "are:")
for i in range(2, user_int):
    if user_int % i == 0:
        print(i)
