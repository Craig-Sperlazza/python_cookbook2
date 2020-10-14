import json

#json object will convert into dict
state_json = '''{
  "states": [
    {
      "name": "Alabama",
      "abbreviation": "AL",
      "area_codes": ["205", "251", "256", "334", "938"]
    },
    {
      "name": "Alaska",
      "abbreviation": "AK",
      "area_codes": ["907"]
    }]
}'''


# we can turn that json string into a python object as follows (look at the individual items to see all the conversions):
# JSON	        Python
# object	    dict
# array	        list
# string	    str
# number(int)	int
# number(real)	float
# true	        True
# false	        False
# null	        None
data = json.loads(state_json)

# print(data)
# print(type(data))

#to access each state or delete a key:value pair:
for state in data['states']:
    print(state['name'])
    print(state['area_codes'])
    del state['abbreviation']

#to convert back to json----indent makes it easier to read, sort_keys sorts the keys for each state alphabetically
new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)