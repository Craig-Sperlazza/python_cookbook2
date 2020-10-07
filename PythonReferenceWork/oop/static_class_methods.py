class Person:
    # class variables
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    def __repr__(self):
        return f"Person({self.name}, {self.age})"

    def __repr__(self):
        return f"{self.name}, {self.age}"

    @classmethod
    def get_population(cls):
        return cls.population

    @staticmethod
    def is_adult(age):
        return age >= 18

    def display(self):
        print(f"{self.name} is {self.age} years old")


print(Person.get_population())
p1 = Person("Craig", 18)
p2 = Person("John", 13)
print(p2.is_adult(p2.age))
print(p1.is_adult(p1.age))
print(Person.get_population())

p1.display()

print(p1)
