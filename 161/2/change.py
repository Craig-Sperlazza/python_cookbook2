# project-2c

# Author: Craig Sperlazza
# Date: 10/7/2019
# Description: Asks the user for a number of cents(integer from 0 to 99) and prints out the type and amount of coins the user would receive

print("Please enter an amount in cents less than a dollar.")
user_number = int(input())

quarter = user_number // 25 #This floor division assigns the amount of quarters (i.e. number of times evenly divided by 25) to the quarter variable
quarter_remainder = user_number % 25 #The modulo operator is the used to get the number remaining after all possible quarters (25) were removed from the total.

dime = quarter_remainder // 10 #The program then moves to the next largest coin, the dime(10) and repeats the above logic.
dime_remainder = quarter_remainder % 10

nickel = dime_remainder // 5
nickel_remainder = dime_remainder % 5

penny = nickel_remainder // 1

print("Your change will be:")
print("Q:", quarter)
print("D:", dime)
print("N:", nickel)
print("P:", penny)
