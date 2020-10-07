# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


list1 = [1, 2, 3, 4, 5]
list2 = [9, 10, 11]

print(max(list1))

print(min(list2))

print(7 in list1)

print(9 in list2)

print(9 not in list2)

print(f"The length of list 1 is: {len(list1)}")

print(f"The sum of list 2 is: {sum(list2)}")


list1.append(7)

print(list1)

list2.extend(list1)

print(list2)

print(max(list1))

print(min(list2))

list1.insert(0, 33)

print(list1)

list1.pop()  # removes from end
list1.pop(0)  # removes form specified index

print(list1)

new_list = [45, 66, 34, 36, 77, 88, 2, 11]

new_list.sort()

print(new_list)

new_list2 = [45, 66, 34, 36, 77, 88, 2, 11]

new_list3 = sorted(new_list2)

print(new_list2)
print(new_list3)
