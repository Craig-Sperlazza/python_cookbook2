#https://www.youtube.com/watch?v=Fw7u3fKFDqI

import timeit


# input_list = range(100)

# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else: 
#         return False

# func_generator = list((i for i in input_list if div_by_five(i)))

# list_comprehension = [i for i in input_list if div_by_five(i)]

#time the function generator with 50000 executions
print(timeit.timeit('''input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else: 
        return False

func_generator = (i for i in input_list if div_by_five(i))''', number=50000))

# #time the list comprehension
print(timeit.timeit('''input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else: 
        return False

list_comprehension = [i for i in input_list if div_by_five(i)]''', number=50000))


#time the function generator with 50000 executions but make it into a list
print(timeit.timeit('''input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else: 
        return False

func_generator = list((i for i in input_list if div_by_five(i)))''', number=50000))