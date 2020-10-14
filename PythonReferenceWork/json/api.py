import json
from urllib.request import urlopen


url = "https://cat-fact.herokuapp.com/facts"
with urlopen(url) as response:
    source = response.read()

data = json.loads(source)

# print(json.dumps(data, indent=2))

names_facts = dict()

for item in data['all']:
    cool_fact = item['text']
    user_name = item['user']['name']['first']
    # print(cool_fact)
    # print(user_name)
    # print(f"User {user_name} submitted the following cool cat fact: {cool_fact} \n")



with open('/home/craig/Desktop/python_cookbook2/PythonReferenceWork/json/cat_facts.json', 'w') as f:
    json.dump(data, f, indent=2)