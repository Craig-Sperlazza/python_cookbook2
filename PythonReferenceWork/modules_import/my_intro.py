import my_module as mm

# if you only want to import the function
from my_module import find_index, test

import sys

courses = ["Math", "Art", "CompSci", "Tech"]

index = mm.find_index(courses, "Math")
print(index)

index2 = find_index(courses, "Art")
print(index2)

print(test)


print(sys.path)
