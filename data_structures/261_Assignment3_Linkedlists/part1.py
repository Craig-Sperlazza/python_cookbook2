def add_link_before(self, data, index):
    """
    Adds a new link containing data and inserts it before the link at index.
    If index is 0, it inserts at the beginning of the list.

    Args:
        data: The data the new node will contain
        index: The index of the node that will immediately follow the newly added node
    """
    new_link = SLNode()  # initialize a new link
    new_link.data = data  # set new_link data

    i = 0
    current = self.head
    previous = self.head

    if index == 0:
        self.add_front(data)
    else:
        while i < index + 1:
            if current.next == self.tail and index >= i + 1:
                raise Exception("Index out of bounds")
            elif i == index:
                new_link.next = current.next
                current.next = new_link
                return
            else:
                previous = current
                current = current.next
                i += 1


def remove_link(self, index):
    """
    Removes the link at the location specified by index
    Args:
        Index: The index of the node that will be removed
    """
    i = 0
    current = self.head
    previous = self.head

    if index < 0:
        raise Exception("Index out of bounds LESS 0")

    elif index == 0:
        current = current.next
        self.head.next = current.next
    else:
        while i < index + 1:
            if current.next == self.tail and index >= i + 1:
                raise Exception("Index out of bounds TOO FAR")
            elif i == index:
                previous = current
                current = current.next
                previous.next = current.next
                return
            else:
                previous = current
                current = current.next
                i += 1


def add_front(self, data):
    """
    Adds a new node after the head that contains data

    Args:
        data: The data the new node will contain
    """
    new_link = SLNode()  # initialize a new link
    new_link.data = data  # set new_link data

    if self.head.next == self.tail:
        # Link the new node to tail
        new_link.next = self.head.next

        # The new node follows head.
        self.head.next = new_link

    else:
        # set the new link next equal to tail
        new_link.next = self.tail
        new_link.next = self.head.next

        # The new node follows head
        self.head.next = new_link


def add_back(self, data):
    """
    Adds a new node before the tail that contains data

    Args:
        data: The data the new node will contain
    """
    new_link = SLNode()  # initialize a new link
    new_link.data = data  # set new_link data


    # if the list is empty but for the sentinels
    if self.head.next == self.tail:
        new_link.next = self.head.next  # set the new node next to tail
        self.head.next = new_link  # set the head next to the new node
    else:
        new_link.next = self.tail
        current = self.head
        # need to loop through the linked list until you get to the element
        # before the tail
        while current.next != self.tail:
            current = current.next
        current.next = new_link


def get_front(self):
    """
    Returns the data in the element at the front of the list. Will return
    None in an empty list.

    Returns:
        The data in the node at index 0 or None if there is no such node
    """

    # if self.head.next.data == None:
    #     return None
    if self.head.next == self.tail:
        return None
    else:
        return self.head.next.data


def get_back(self):
    """
    Returns the data in the element at the end of the list. Will return
    None in an empty list.

    Returns:
        The data in the node at last index of the list or None if there is no such node
    """
    # if the list is empty but for the sentinels
    if self.head.next == self.tail:
        return None
    else:
        current = self.head
        # need to loop through the linked list until you get to the element
        # before the tail
        while current != self.tail:
            if current.next == self.tail:
                return current.data
            else:
                current = current.next


def remove_front(self):
    """
    Removes the first element of the list. Will not remove the tail.
    """

    # if self.head.next.data == None:
    #     return
    if self.head.next == self.tail:
        return
    else:
        current = self.head.next
        self.head.next = current.next


def remove_back(self):
    """
    Removes the last element of the list. Will not remove the head.
    """

    # if the list is empty but for the sentinels
    if self.head.next == self.tail:
        return
    else:
        current = self.head
        previous = self.head
        # need to loop through the linked list until you get to the element
        # before the tail
        while current != self.tail:
            if current.next == self.tail:
                previous.next = current.next
                return
            else:
                previous = current
                current = current.next


def is_empty(self):
    """
    Checks if the list is empty

    Returns:
        True if the list has no data nodes, False otherwise
    """

    if self.head.next == self.tail:
        return True
    elif self.head.next != self.tail:
        return False


def contains(self, value):
    """
    Checks if any node contains value

    Args:
        value: The value to look for

    Returns:
        True if value is in the list, False otherwise
    """
    # return false if the list is empty
    if self.head.next == self.tail:
        return False
    elif self.head.next != self.tail:
        current = self.head.next
        # if value is the first data node return true
        if current.data == value:
            return True
        else:
            # iterate throough the list
            while current.next != self.tail:
                current = current.next
                if current.data == value:
                    return True
                current = current.next
        return False


def remove(self, value):
    """
    Removes the first instance of an element from the list

    Args:
        value: the value to remove
    """

    current = self.head
    previous = self.head

    while current.next != self.tail:
        if current.data == value:
            previous.next = current.next
            return
        else:
            previous = current
            current = current.next
