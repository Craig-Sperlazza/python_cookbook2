#print a list seperate by commas---flexible to grow with size of lsit and change delimiter

from typing import List, Tuple, Dict, Sequence, Optional, Set


def add_delimit(arr: list, delimit: str) -> str:
    """[summary]

    Args:
        arr (list): list to be joined into a string
        delimit (str): string delimiter to seperate items of the list

    Returns:
        str: [description]
    """
    new_str: str = delimit.join(arr)
    return new_str

if __name__ == "__main__":
    test: list = ['a', 'c', 'd', 'e']

    DELIMITER: str = ","

    result: str = add_delimit(test, DELIMITER)

    print(result)