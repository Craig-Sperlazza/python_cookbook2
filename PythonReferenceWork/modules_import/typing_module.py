# https://www.pythonsheets.com/notes/python-typing.html

#type checking may work better with pycharm

from typing import List, Tuple, Dict, Sequence, Optional, Set

name: str = "Craig"

number: int = 123

float_number: float = 1.754

#####iterables##################
mixed_list: List = [1, "red"]

new_list_int: List[int] = [1, 2, 3]
new_list_int.append("Red")
print(new_list_int)

second_list_int: List[int] = [i for i in range(10)]

new_list_str: List[str] = ["red", "green"]

new_set: Set = {1, 2, 3, 3}

new_tuple: Tuple[int, int, int, str] = (1, 2, 3, 'red')

new_dict: Dict[str, str] = {"color": "red"}

############optional means a data type can be None

var_optional: Optional[int] = None 
var_optional = 3

###############FUNCTION####################
def add_two(a: int, b: int) -> int:
    return a + b
print(add_two('red', 3))



