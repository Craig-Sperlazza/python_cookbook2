# hash_map.py
# ===================================================
# Implement a hash map with chaining
# ===================================================

class SLNode:
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value

    def __str__(self):
        return '(' + str(self.key) + ', ' + str(self.value) + ')'

    # def __cmp__(self, other):
    #     if hasattr(other, 'value'):
    #         return self.value.__cmp__(other.value)
    #
    # def __lt__(self, other):
    #     return self.value < other.value
    #
    # def __gt__(self, other):
    #     return self.value > other.value
    #
    # def __eq__(self, other):
    #     return self.value == other.value


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_front(self, key, value):
        """Create a new node and inserts it at the front of the linked list
        Args:
            key: the key for the new node
            value: the value for the new node"""
        new_node = SLNode(key, value)
        new_node.next = self.head
        self.head = new_node
        self.size = self.size + 1

    def remove(self, key):
        """Removes node from linked list
        Args:
            key: key of the node to remove """
        if self.head is None:
            return False
        if self.head.key == key:
            self.head = self.head.next
            self.size = self.size - 1
            return True
        cur = self.head.next
        prev = self.head
        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                self.size = self.size - 1
                return True
            prev = cur
            cur = cur.next
        return False

    def contains(self, key):
        """Searches linked list for a node with a given key
        Args:
        	key: key of node
        Return:
        	node with matching key, otherwise None"""
        if self.head is not None:
            cur = self.head
            while cur is not None:
                if cur.key == key:
                    return cur
                cur = cur.next
        return None

    def __str__(self):
        out = '['
        if self.head != None:
            cur = self.head
            out = out + str(self.head)
            cur = cur.next
            while cur != None:
                out = out + ' -> ' + str(cur)
                cur = cur.next
        out = out + ']'
        return out


def hash_function_1(key):
    hash = 0
    for i in key:
        hash = hash + ord(i)
    return hash


def hash_function_2(key):
    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash


class HashMap:
    """
    Creates a new hash map with the specified number of buckets.
    Args:
        capacity: the total number of buckets to be created in the hash table
        function: the hash function to use for hashing values
    """

    def __init__(self, capacity, function):
        self._buckets = []
        for i in range(capacity):
            self._buckets.append(LinkedList())
        self.capacity = capacity
        self._hash_function = function
        self.size = 0

    def clear(self):
        """
        Empties out the hash table deleting all links in the hash table.
        """

        for linked_list in self._buckets:
            linked_list.head = None
            linked_list.size = 0
        self.size = 0
        return

    def get(self, key):
        """
        Returns the value with the given key.
        Args:
            key: the value of the key to look for
        Return:
            The value associated to the key. None if the link isn't found.
        """
        hash_key = self._hash_function(key)
        # find the bucket for hash
        index = hash_key % (self.capacity)
        bucket = self._buckets[index]

        contains_key = bucket.contains(key)

        if contains_key is None:
            return None
        else:
            return contains_key.value

    def resize_table(self, capacity):
        """
        Resizes the hash table to have a number of buckets equal to the given
        capacity. All links need to be rehashed in this function after resizing
        Args:
            capacity: the new number of buckets.
        """
        #copy old linked lists over
        copy_items = []
        for linked_list in self._buckets:
            current_node = linked_list.head
            while current_node is not None:
                copy_items.append(current_node)
                current_node = current_node.next

        #make a bigger capacity hash table
        self._buckets = []
        for i in range(capacity):
            self._buckets.append(LinkedList())
        self.capacity = capacity
        self.size = 0

        #add nodes
        for node in copy_items:
            self.put(node.key, node.value)
        return


    def put(self, key, value):
        """
        Updates the given key-value pair in the hash table. If a link with the given
        key already exists, this will just update the value and skip traversing. Otherwise,
        it will create a new link with the given key and value and add it to the table
        bucket's linked list.

        Args:
            key: they key to use to has the entry
            value: the value associated with the entry
        """
        #find the hash value for the key
        hash_key = self._hash_function(key)
        #find the bucket for hash
        index = hash_key % self.capacity
        bucket = self._buckets[index]

        contains_key = bucket.contains(key)

        if contains_key != None:
            bucket.remove(key)
            bucket.add_front(key, value)
        else:
            bucket.add_front(key, value)
            self.size += 1


    def remove(self, key):
        """
        Removes and frees the link with the given key from the table. If no such link
        exists, this does nothing. Remember to search the entire linked list at the
        bucket.
        Args:
            key: they key to search for and remove along with its value
        """
        hash_key = self._hash_function(key)
        # find the bucket for hash
        index = hash_key % (self.capacity)
        bucket = self._buckets[index]

        contains_key = bucket.contains(key)

        if contains_key is None:
            return None
        else:
            bucket.remove(key)

    def contains_key(self, key):
        """
        Searches to see if a key exists within the hash table

        Returns:
            True if the key is found False otherwise

        """
        hash_key = self._hash_function(key)
        # find the bucket for hash
        index = hash_key % (self.capacity)
        bucket = self._buckets[index]

        contains_key = bucket.contains(key)

        if contains_key is None:
            return False
        else:
            return True

        ##########################################
        # for linked_list in self._buckets:
        #     if linked_list.contains(key) is None:
        #         return False
        # return True


    def empty_buckets(self):
        """
        Returns:
            The number of empty buckets in the table
        """
        empty = 0

        for linked_list in self._buckets:
            if linked_list.head is None:
                empty = empty + 1
        return empty

    def table_load(self):
        """
        Returns:
            the ratio of (number of links) / (number of buckets) in the table as a float.

        """
        return float(self.size) / self.capacity

    def __str__(self):
        """
        Prints all the links in each of the buckets in the table.
        """

        out = ""
        index = 0
        for bucket in self._buckets:
            out = out + str(index) + ': ' + str(bucket) + '\n'
            index = index + 1
        return out

# #resize testing 1 passing
# m = HashMap(20, hash_function_1)
# m.put('key1', 10)
# print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
# m.resize_table(30)
# print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))


# # #resize testing 2 passing
# m = HashMap(75, hash_function_2)
# keys = [i for i in range(1, 1000, 13)]
# for key in keys:
#     m.put(str(key), key * 42)
# print(m.size, m.capacity)
# for capacity in range(111, 1000, 117):
#     m.resize_table(capacity)
#     result = True
#     for key in keys:
#         result = result and m.contains_key(str(key))
#         result = result and not m.contains_key(str(key + 1))
#     print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))


# #clear testing 1 passing
# m = HashMap(100, hash_function_1)
# print(m.size, m.capacity)
# m.put('key1', 10)
# m.put('key2', 20)
# m.put('key1', 30)
# print(m.size, m.capacity)
# print(m)
# m.clear()
# print(m)
# print(m.size, m.capacity)


# #clear testing 2 passing except for the resize portion
# m = HashMap(50, hash_function_1)
# print(m.size, m.capacity)
# m.put('key1', 10)
# print(m.size, m.capacity)
# m.put('key2', 20)
# print(m.size, m.capacity)
# m.resize_table(100)
# print(m.size, m.capacity)
# print(m)
# m.clear()
# print(m)
# print(m.size, m.capacity)


# # put testing example 1---passing
# m = HashMap(50, hash_function_1)
# for i in range(150):
#     m.put('str' + str(i), i * 100)
#     # print(m)
#     if i % 25 == 24:
#         print(m.empty_buckets(), m.table_load(), m.size, m.capacity)
#         # print(m)

#put testing example 2---passing
# m2 = HashMap(40, hash_function_2)
# for i in range(50):
#     m2.put('str' + str(i // 3), i * 100)
#     # print(m2)
#     if i % 10 == 9:
#         print(m2.empty_buckets(), m2.table_load(), m2.size, m2.capacity)
#         #print(m2)

# # contains function testing---passing except last one relies on remove
# m = HashMap(50, hash_function_1)
# print(m.contains_key('key1'))
# m.put('key1', 10)
# m.put('key2', 20)
# m.put('key3', 30)
# # print(m)
# print(m.contains_key('key1'))
# print(m.contains_key('key4'))
# print(m.contains_key('key2'))
# print(m.contains_key('key3'))
# m.remove('key3')
# print(m.contains_key('key3'))


# #contains testing 2
# m = HashMap(75, hash_function_2)
# keys = [i for i in range(1, 1000, 20)]
# for key in keys:
#     m.put(str(key), key * 42)
# print(m.size, m.capacity)
# result = True
# for key in keys:
#     # all inserted keys must be present
#     result = result and m.contains_key(str(key))
#     # all NOT inserted keys must be absent
#     result = result and not m.contains_key(str(key + 1))
# print(result)

# # empty buckets ---passing
# m = HashMap(100, hash_function_1)
# print(m.empty_buckets(), m.size, m.capacity)
# m.put('key1', 10)
# print(m.empty_buckets(), m.size, m.capacity)
# m.put('key2', 20)
# print(m.empty_buckets(), m.size, m.capacity)
# m.put('key1', 30)
# print(m.empty_buckets(), m.size, m.capacity)
# m.put('key4', 40)
# print(m.empty_buckets(), m.size, m.capacity)

# #empty buckets 2 passing
# m = HashMap(50, hash_function_1)
# for i in range(150):
#     m.put('key' + str(i), i * 100)
#     if i % 30 == 0:
#         print(m.empty_buckets(), m.size, m.capacity)

# #table load test 1 passing
# m = HashMap(100, hash_function_1)
# print(m.table_load())
# m.put('key1', 10)
# print(m.table_load())
# m.put('key2', 20)
# print(m.table_load())
# m.put('key1', 30)
# print(m.table_load())

# # table load test 2 passing
# m = HashMap(50, hash_function_1)
# for i in range(50):
#     m.put('key' + str(i), i * 100)
#     if i % 10 == 0:
#         print(m.table_load(), m.size, m.capacity)

# #get testing 1 passing
# m = HashMap(30, hash_function_1)
# print(m.get('key'))
# m.put('key1', 10)
# print(m.get('key1'))

# #get testing 2 passing
# m = HashMap(150, hash_function_2)
# for i in range(200, 300, 7):
#     m.put(str(i), i * 10)
# print(m.size, m.capacity)
# for i in range(200, 300, 21):
#     print(i, m.get(str(i)), m.get(str(i)) == i * 10)
#     print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

# #remove test 1 passing
# m = HashMap(50, hash_function_1)
# print(m.get('key1'))
# m.put('key1', 10)
# print(m.get('key1'))
# m.remove('key1')
# print(m.get('key1'))
# m.remove('key4')
