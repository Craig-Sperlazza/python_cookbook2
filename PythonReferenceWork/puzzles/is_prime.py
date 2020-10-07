#This is a prime number checker from Professors lecture

num = int(input("Please enter a positive integer."))

#start out assuming that num is prime
is_prime = True

#deal with 1 which is a special case, if num == 1, it is not prime
if (num == 1):
    is_prime = False

#otherwise divide num by 2 through num - 1
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False

#print the conclusion
if(is_prime):
    print(num, "is prime")
else:
    print(num, "is NOT prime")
