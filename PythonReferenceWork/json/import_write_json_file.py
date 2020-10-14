import json

#note load() method loads a json file, loads() loads a string (see basic example)

with open('/home/craig/Desktop/python_cookbook2/PythonReferenceWork/json/states.json', 'r') as f:
    data = json.load(f)
    
for state in data['states']:
    print(state)
    print(state['name'], state['abbreviation'])
        

#write your python object to a json file in json format
# we are going to remove area codes and then write it to 'new_states.json'
#json.dump(object_to_dump, file_to_dump_to)

for state in data['states']:
    del state['area_codes']

with open('/home/craig/Desktop/python_cookbook2/PythonReferenceWork/json/new_states.json', 'w') as f:
    json.dump(data, f, indent=2)