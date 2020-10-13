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
