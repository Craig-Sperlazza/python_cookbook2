
from util import hash_func as hf
from util import list_func as lf

test_list = [1, 6, 33, 55, 2, 77]

test_hash = {"weight": 333, "height": 68}

hf.get_key_value(test_hash)

list_avg = lf.get_avg(test_list)

sort_lst = lf.get_sort(test_list)

print(list_avg)
print(sort_lst)