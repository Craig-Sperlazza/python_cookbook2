# word_count.py
# ===================================================
# Implement a word counter that counts the number of
# occurrences of all the words in a file. The word
# counter will return the top X words, as indicated
# by the user.
# ===================================================

import re
from hash_map import HashMap

"""
This is the regular expression used to capture words. It could probably be endlessly
tweaked to catch more words, but this provides a standard we can test against, so don't
modify it for your assignment submission.
"""
rgx = re.compile("(\w[\w']*\w|\w)")

def hash_function_2(key):
    """
    This is a hash function that can be used for the hashmap.
    """

    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash

# use hash_function_2 for assignment, this for comparison
def hash_function_1(key):
    hash = 0
    for i in key:
        hash = hash + ord(i)
    return hash

def top_words(source, number):
    """
    Takes a plain text file and counts the number of occurrences of case insensitive words.
    Returns the top `number` of words in a list of tuples of the form (word, count).

    Args:
        source: the file name containing the text
        number: the number of top results to return (e.g. 5 would return the 5 most common words)
    Returns:
        A list of tuples of the form (word, count), sorted by most common word. (e.g. [("a", 23), ("the", 20), ("it", 10)])
    """

    keys = set()

    ht = HashMap(2500,hash_function_1)

    # This block of code will read a file one word as a time and
    # put the word in `w`. It should be left as starter code.
    with open(source) as f:
        for line in f:
            words = rgx.findall(line)
            for w in words:
                #strip leading and trailing whitespace
                w = w.strip()
                #strip away punctuation
                #characters taken from:
                #https://www.programiz.com/python-programming/examples/remove-punctuation
                w = w.strip('''!()-[]{};:'"\,<>./?@#$%^&*_~''')
                #make it lowercase
                w = w.lower()
                word_exists = ht.contains_key(w)
                if word_exists == False:
                    ht.put(w, 1)
                elif word_exists == True:
                    #get value
                    num_occurence = ht.get(w)
                    ht.remove(w)
                    num_occurence += 1
                    ht.put(w, num_occurence)

    # # prints bucket by bucket
    # for i in ht._buckets:
    #     print(i)
    # print(ht.size)
    # print(ht.capacity)

    new_list = []
    for linked_list in ht._buckets:
        current_node = linked_list.head
        while current_node is not None:
            new_list.append(current_node)
            current_node = current_node.next
    # for i in new_list:
    #     print(i)

    #bubble sort was taken from the lecture
    l = len(new_list)
    for a in range(l):
        for b in range(l - 1):
            if (new_list[a].value is None or new_list[b].value is None):
                pass
            elif (new_list[a].value > new_list[b].value):
                new_list[a], new_list[b] = new_list[b], new_list[a]

    return_list = []
    count = 0
    #while count < number:
    for num in new_list:
        if count < number:
            tup1 = (num.key, num.value)
            return_list.append(tup1)
            count += 1
        else:
            break
    return return_list

print(top_words("alice.txt",10))  # COMMENT THIS OUT WHEN SUBMITTING TO GRADESCOPE
# print(top_words("alice.txt",15))