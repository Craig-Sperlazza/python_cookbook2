"""
#create an empty dictionary
dict = {}

print(type(dict))

#add items to the dictionary
dict['kid'] = 'Henrik'
dict['sport'] = 'Wrestling'
dict['age'] = 10
dict['weight'] = 91.2
print(dict)

#add a new key:value
dict['school'] = 'midland'
print(dict)

#retrieve a value using the key
print(dict['kid'])
print(dict['sport'])
print(dict['age'], dict['weight'])

#loop through a dictionary without using the items, key, value functions
eng_to_span = {"one": "uno",
               "two": "dos",
               "three": "tres",
               "four": "cuatro",
               "five": "cinco",
               "six": "seis",
               "seven": "siete",
               "eight": "ocho",
               "nine": "nueve",
               "ten": "diez"}

for n in eng_to_span:
  print(n, eng_to_span[n]) #will print key value

for n in eng_to_span:
    print(n) # will print key

for n in eng_to_span:
    print(eng_to_span[n]) # will print value


#loop through a dictionary and print the value by referencing a [key]
for k in dict.keys():
    print(dict[k])

#loop through a dictionary and print the value using values()
for v in dict.values():
    print(v)

#loop through a dictionary and print the key by using keys()
for k in dict.keys():
    print(k)

#loop through a dictionary and print the key:value pair----Two seperate print methods
for k, v in dict.items():
    print(k, ':', v)

for k, v in dict.items():
    print("{}: {}".format(k, v))

#hashing from two arrays of equal length

arr_1 = [1, 2, 3, 4]
arr_2 = ['cat', 'dog', 'rat', 'snake']

new_dict = {k:v for k, v in zip(arr_1, arr_2)}

print(new_dict)

"""
#loop through a dictionary without using the items, key, value functions
eng_to_span = {"prizes":[{"one": "uno",
               "two": "dos"},
                {"three": "tres",
                "four": "cuatro"}]}

year = {"one": "uno",
               "two": "dos"}
for n in eng_to_span:
    if eng_to_span[n][0] == year:
        print(eng_to_span[n][0]) # prizes/key


"""
for n in eng_to_span:
  print(n, eng_to_span[n]) #will print key value

for n in eng_to_span:
    print(n) # will print key

for n in eng_to_span:
    print(eng_to_span[n]) # will print value

for v in eng_to_span.values():
    print(v)

#loop through a dictionary and print the key by using keys()
for k in eng_to_span.keys():
    print(k)

#loop through a dictionary and print the key:value pair----Two seperate print methods
for k, v in eng_to_span.items():
    print(k, ':', v)
"""