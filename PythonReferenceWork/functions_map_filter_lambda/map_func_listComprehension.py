from functools import reduce

# functional programming---map function

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def my_func(x):
    return x**x

# we want to apply the function to each value and hav eit stored in a new list
# traditionally use for loop but we can use map(function, list)


print(list(map(my_func, li)))

print(li)

new_li = list(map(my_func, li))
print(new_li)

# can also use a list comprehension
print([my_func(x) for x in li])

# can also make conditionals
print([my_func(x) for x in li if x % 2 == 0])


# can also pass a lambda function into map

lambda_list = list(map(lambda x: x + x, li))
print(lambda_list)

#map example, make all items upper()
pet = ['bella', 'bodhi', 'rando', 'togi']

pet2 = list(map(str.upper, pet))
print(pet2)

#round numbers
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
round_areas = list(map(round, circle_areas)) #i cant figure our how to pick a roudning range
print(round_areas)
round_comp = [round(x, 2) for x in circle_areas]
print(round_comp)

#use a comprehension to make a bunch of string values integers
str_lst = ['1', '2', '3']
print(str_lst)
int_lst = [int(x) for x in str_lst]
print(int_lst)


print('#####################################################')

map_fun = [1, 2, 3, 4, 5, 6, 7, 8]


even_plus_two = list(map(lambda x: x + 2, filter(lambda i: i % 2 ==0, map_fun)))
print(even_plus_two)


make_odd = map(lambda x: x + 1, even_plus_two)
print(list(make_odd))

print('#####################################################')

numbers = [1,2,3,4,5,6,7,8,9,10]

# odd_numbers = list(filter(lambda x: x%2 != 0, numbers))

# print(odd_numbers)

# square_odd_numbers = list(map(lambda x: x**2, odd_numbers))
# print(square_odd_numbers)

# total = reduce(lambda acc, x: acc + x, square_odd_numbers)
# average = reduce(lambda acc, x: acc + x, square_odd_numbers)/len(square_odd_numbers)
# print(total)
# print(average)

odd_numbers = list(filter(lambda x: x % 2 !=0, numbers))
square_odd = list(map(lambda x: x **2, odd_numbers))
total = reduce(lambda acc, x: acc + x, square_odd)
average = (reduce(lambda acc, x: acc + x, square_odd)) / len(square_odd)

print('#####################################################')

arr_1 = [1, 2, 3]
arr_2 = [4, 5, 6]

sum_arr = list(map(lambda x, y: x + y, arr_1, arr_2))
print(sum_arr)
