# List comprehension is an elegant way to define and create
# lists based on existing lists.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

first_col_each_row = [row[0] for row in matrix]
print(first_col_each_row)

second_col = [i[1] for i in matrix]
print(second_col)

third_col = [row[2] for row in matrix]
print(third_col)

# add letters of 'human' to a list

human_lst = [letter for letter in 'human']
print(human_lst)


# List Comprehension
# This technique allows you to quickly create lists with a single line of code.
# You can think of this as deconstructing a for loop with an append(). For Example:

# Starting with:
x = [1, 2, 3, 4]

# We could do this:
out = []
for item in x:
    out.append(item**2)
print(out)


# Written in List Comprehension Form
[item**2 for item in x]

# List Comprehension is a great tool, but remember its not always approriate for
# every situation, don't sacrafice readability for a list Comprehension. It's
# speed is very comparable to the for loop.
