#hash functions

from typing import Dict

def get_key(dict: Dict) -> None:
    for i in dict.keys():
        print(i)

def get_value(dict: Dict)-> None:
    for v in dict.values():
        print(v)

def get_key_value(dict: Dict)-> None:
    for i, v in dict.items():
        print(f"{i}:{v}")



if __name__ == "__main__":
    test_dict = {"name": "James", "age": 37}

    get_key(test_dict)

    get_value(test_dict)

    get_key_value(test_dict)
