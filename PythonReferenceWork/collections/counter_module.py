# https://www.youtube.com/watch?v=cgDRugJzBfM&list=PLzMcBGfZo4-nhWva-6OVh1yKWHBs4o_tv&index=6

import collections
from collections import Counter


# Python containers incllude:
# list, set, dict, tuple (immutable)

# types in collections
# counter----Counter returns a counter object
# deque
# namedTuple()
# orderedDict
# defaultDict

c = Counter('gallad')
print("string counter", c)

c1 = Counter(['a', 'b', 'c', 'd', 'a'])
print("list counter", c1)

# with dictionary you can do either 
c2 = Counter({'cats':1, 'dogs':2})

c3 = Counter(cats=4, dogs=7, rats=3)
print("dict counter:", c2)
print("dict counter type 2:", c3)

# to pick specific keys and print their values---will give you back 0 instead of throwing an error if it does not exist
print(c2['dogs'])
print(c2['turtles'])

#this will returns a list with: cats 4 times, dogs 7 times, rats 3 times
print(list(c3.elements()))

#get the most common elements (specifiy if you want the most common (1), two most common (2), etc.  )
#returns a tuple ('a', 2)
print(c1.most_common(1))


#can also add or subtract counts from a counter object
d = Counter({'boys': 3, 'girls': 2})

e = {'boys':1}
f = {'girls': 5}

d.subtract(e)
print(d)

d.update(f)
print(d)

#another example with string
x = Counter("Witcher")
y = "cer"
x.subtract(y)
print(x)

#this clears the counter object
x.clear()
print(x)

#you can also add, substract, union, intersection of counters too
m = Counter({'a':2, 'b':5})
n = Counter(a=4, b=7)

print(m+n)
print(n-m)

#intersection (minimum like elements in both)
print(m & n)

#union(max elements in either)
print(m | n)
