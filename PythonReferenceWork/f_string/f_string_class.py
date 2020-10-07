class Comedian:
    def __init__(self, f_name, l_name, age):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age

    def __str__(self):
        return f"{self.f_name} {self.l_name} {self.age}."

    def __repr__(self):
        return f"{self.f_name} {self.l_name} {self.age}."


first_comedian = (Comedian("Eric", "Smith", 40))

print(first_comedian)

print(f"Here is the info on the first comedian: {first_comedian}")


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"The make is {self.make}, the model is {self.model}, and the year is {self.year}"

    def __repr__(self):
        return f"The make is {self.make}, the model is {self.model}, and the year is {self.year}"


car1 = (Car('Ford', 'Explorer', 2014))

print(car1)

print(f"The first car is {car1}")
