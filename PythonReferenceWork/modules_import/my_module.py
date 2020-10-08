print("Imported my_module")

test = "test string"


def find_index(to_search, target):
    """find the index of a value in a sequence using enumerate()

    Args:
        to_search ([type]): [description]
        target ([type]): [description]
    """
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1


# print(find_index(test, "s"))
