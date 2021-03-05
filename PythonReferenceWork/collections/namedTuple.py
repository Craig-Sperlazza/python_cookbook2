# https://www.youtube.com/watch?v=GKgpvriuQY8&list=PLzMcBGfZo4-nhWva-6OVh1yKWHBs4o_tv&index=7

import collections
from collections import namedtuple

#name of the tuple is Point and it has the fields x, y, z
Point = namedtuple('Point', ['x', 'y', 'z'])

p1 = Point(5, 10, 3)
p2 = Point(15, 11, 7)

print(p1)
print(p2)

#access individual elements
print(p1.z)

#use same basic operations we use on tuples
print(p1[0])

#print it as a dictionary
print(p1._asdict())

#print out a tuple with just field names
print(p1._fields)

#replace method but must assign to a new name
p3 = p1._replace(y=6)
print(p3)