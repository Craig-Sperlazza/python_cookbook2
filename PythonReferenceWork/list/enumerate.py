# Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
# This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.

# Syntax:

# enumerate(iterable, start=0)

# Parameters:
# Iterable: any object that supports iteration
# Start: the index value from which the counter is
#               to be started, by default it is 0

l1 = [1, 2, 3, 4, 5, 6]

obj1 = enumerate(l1)
print(list(obj1))  # will print a list of tuple where each tuple is (i, value)

# 0 is the default start of the iterator but you can change it (here we start at 10)
obj2 = enumerate(l1, 10)
print(list(obj2))


# using the enumerate object in loops
l2 = ['a', 'b', 'c', 'd']

obj3 = enumerate(l2, 100)
print(list(obj3))
new_list2 = list(obj3)


for i, value in enumerate(l2, 100):
    print(f'the index is {i}')
    print(f'the value is {value}')
