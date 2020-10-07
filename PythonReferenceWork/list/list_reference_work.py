#create an empty list
list1 = []

#create a list
list2 = [2, 4, 6, 8]

#####Different ways to add to beginning of a list#############################


list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]

def insert_front(user_list, item):
    """This will add an element to the beingging of the list by shifting them
    NOTE you DO use [item]"""
    user_list[0:0] = [item]

insert_front(list1, 10)

print(list1)

def replace_front(user_list, item):
    """This replaces the first element
    NOTE you DO NOT use [item]"""
    user_list[0] = item
    
replace_front(list2, 10)
 
print(list2)
#############################################################################



#print value or index
list_print = ["shoes", "bananas", "surfing"]
print(list_print[1])  #prints bananas
print(list_print.index("surfing")) #prints 2

#APPEND items to the end of a list
list1.append("red")
list1.append("blue")
list1.append("green")
print(list1)

#INSERT items into a list at a specific index value using listName.insert(index, item)
list1.insert(3, 'purple')
list1.insert(len(list1), 'magenta') #at the end
print(list1)

#DELETE items from a list using index
del list2[0]
print(list2)

#REMOVE items using the value
remove_list = ["jeans", "boots", "socks"]
remove_list.remove("boots")
print(remove_list)


#FIND BY INDEX---prints value
print(list1[1])
print(list1[-1])

#SLICE---prints a list
print(list1[1:3])

"""
for loops with list
"""
# loop and print values
for i in list1:
    print(i)

#loop and print index:value
for k, v in enumerate(list1):
    print(k,':', v)
for k, v in enumerate(list1):
    print("{}: {}".format(k,v))

#loop and print index using range()
for index in range(len(list1)):
    print(index)

#loop and print value using range()
for val in range(len(list1)):
    print(list1[val])

#loop with conditional
spam = ['cat', 'red', 'ball', 'reddit']

for i in range(len(spam)):
    if len(spam[i]) >= 4:
        print(i, spam[i]) #will print 2 ball \n 3 reddit

"""
while loops with lists
"""


"""
SORTING Lists
"""
int_sort = [34, 45, 2, 0, -32, 104]
str_sort = ['cat', 'Dog', 'ball', 'peaches']
str_sort2 = ['cat', 'Dog', 'ball', 'peaches']
str_sort3 = ['carrots', 'Dash', 'belts', 'peas']

#print a sorted list but not sort the list
print(sorted(int_sort))
print(sorted(int_sort, reverse=True))

#sort the list
str_sort.sort(reverse=True)
print(str_sort) #remeber cap letters over lowercase so it prints(peaches, cat, ball, Dog)

#so make it lowercase first
str_sort3.sort(key=str.lower)
print(str_sort3)

"""
JOIN
join() ----" ".join(list) method takes a list and joins it together into a new string
"""
join_list = ["The", "cat", "is", "fast"]

join_string = " ".join(join_list) #joins it with a space ("The cat is fast")
print(join_string)
print(join_list)

join_string2 = ", ".join(join_list) #joins it with a , ("The, cat, is, fast")
print(join_string2)

#comma code---write a function that takes a list value as an argument and returns a string with all the
#items seperated by a comma and a space with "and inserted before the last item

spam = ['apples', 'bananas', 'oranges', 'lemons']

def comma_code2(one_list):
    new_string = ", ".join(one_list[:-1]) +' and ' + one_list[-1]
    print(new_string)
comma_code2(spam)

"""
SPLIT
split() ---.split(string) method takes a string and splits it into a list
"""
split_string = "The cat is amazing at tennis"

split_list = split_string.split(" ") # will split at each space
print(split_list)

split_list2 = split_string.split(" ", 3) #(will make 0, 1, 2, 3 list items)
print(split_list2)