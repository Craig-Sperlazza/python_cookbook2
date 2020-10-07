car1 = {"Make": "Ford", "Model": "Explorer", "Year": 2020}

print(car1)

print(car1["Make"])

car1["Make"] = "Volvo"

keys = car1.keys()
print(keys)

values = car1.values()
print(values)

items = car1.items()
print(items)


# sets
lst1 = [1, 2, 1, 3, 1]

set1 = set(lst1)

print(set1)

print("____________________LOOPS______________________")

for key in car1:
    print(f"The Key Is: {key}")

for key in car1:
    print(f"The Value Is: {car1[key]}")
