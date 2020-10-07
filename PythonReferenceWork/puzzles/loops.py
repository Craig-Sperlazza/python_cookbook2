import random

# simple for loop to print to 5
for i in range(1, 6):
    print(i)

#simple while loop to print to 5
num = 1
while num < 6:
    print(num)
    num += 1

##########################################################################################################

#for loop with range() to print something x times
for i in range(5):
    print("Hi")

#while loop to print something x times
i = 0
while i < 5:
    print("while")
    i += 1
##########################################################################################################


#for loop to add up all the numbers between 1 and 100
count = 0
for i in range(101):
    count = count + i
print(count)

#while loop to add up all the numbers between 1 and 100
num = 0
count3 = 0

while num < 101:
    count3 = count3 + num
    num += 1
print(count3)
########################################################################################################

# for loop for factorials
factorial = int(input("What number do you want the factorial of?\n"))
count1 = 1

for i in range(1, (factorial + 1)):
    count1 = i * count1
print("Using a For Loop: The factorial of {} is {}".format(factorial, count1))

#while loop for factorials
user_num4 = int(input("What number do you want a factorial of? \n"))
count4 = 1
iter4 = 1

while iter4 < (user_num4 + 1):
    count4 = count4 * iter4
    iter4 += 1
print("Using a while loop the factorial of {} is {}".format(user_num4, count4))

################################################################################################################
"""
#break statement
while True:
    play = input("Type Y to play")
    play2 = play.lower()
    if play2 == "y":
        print("Thanks for playing")
        #break (if you have a break here it plays once and ends, if not it keeps prompting you
    else:
        print("goodbye")
"""
"""
#break/continue
while True:
    name = input("What is your name?")
    name = name.lower()
    if name != "craig": # if the name is wrong, it reprompts them
        continue
    else:
        password = input("What is your password?")
        if password == "SurfingUSA": #if the password is wrong, it goes back to the name prompt
            break
print("Welcome Craig!")
"""

#loop to print prime numbers between 2 and x

def is_prime():
    num = input("Please input a number to see if it is a prime number: \n")
    num = int(num)
    divsors_list = []

    if num < 0 or num == 0 or num == 1:
        print("By definition {} is not a prime".format(num)) #I am not actually sure about negatives, could do an absolute value on the input to fix
    else:
        for i in range(2, num - 1):
            if num % i == 0:
                divsors_list.append(i)

        if divsors_list == []:
            print("{} is a prime that is only divisble by 1 and {}".format(num, num))

        else:
            divsors_list.append(1)
            divsors_list.append(num)
            divsors_list.sort()
            print("{} is not a prime number and is divisible by the following: {}".format(num, divsors_list))

is_prime()



