from typing import List, Optional

import statistics

def get_max(lst: List[int]) -> int:
    return max(lst)

def get_min(lst: List[int]) -> int:
    return min(lst)
    
def get_avg(lst: List[int]) -> float:
    return statistics.mean(lst)

def get_sort(lst: List[int]) -> List[int]:
    new_lst = sorted(lst)
    return new_lst


if __name__ == "__main__":
    test_list = [1, 6, 3, 88, 54, 2, 34, 66]

    print(get_max(test_list))

    print(get_min(test_list))

    print(get_avg(test_list))

    print(get_sort(test_list))