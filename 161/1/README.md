# project-1

Write a class called Person that has two data members - the person's name and age.  It should have an init method that takes two values and uses them to initialize the data members.

Write a separate function (not part of the Person class) called basic_stats that takes as a parameter a list of Person objects and returns a tuple containing the mean, median, and mode of all the ages.  To do this, import the **statistics** library and use its built-in mean, median and mode functions.  Your basic_stats function should return those three values as a tuple, in the order given above.

For example, it could be used as follows:
```
p1 = Person("Kyoungmin", 73)
p2 = Person("Mercedes", 24)
p3 = Person("Avanika", 48)
p4 = Person("Marta", 24)

person_list = [p1, p2, p3, p4]
print(basic_stats(person_list))  # should print a tuple of three values
```

The files must be named: basic_stats.py
