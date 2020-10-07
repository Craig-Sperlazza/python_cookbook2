# ######################
# Lambda Expressions
# ######################

#  You won't always need a full blown function, often you will just want to use
#  a function only once, in some of these cases, it makes more sense to use a
# lambda expression, also known as an anonymous function. Let's see an example:

def timesTwo(num):
    return num*2


# Lambda expression
lambda num: num*2

# To really understand the use case for this, we need to introduce a function
# that accepts other functions as input parameters, in this case, we will use filter:
#
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def evenBool(num):
    return num % 2 == 0


evens = filter(evenBool, my_list)
print(list(evens))

# Now with Lambda!
evens = filter(lambda num: num % 2 == 0, my_list)
print(list(evens))
