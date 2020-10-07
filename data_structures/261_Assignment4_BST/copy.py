# bst.py
# ===================================================
# Implement a binary search tree that can store any
# arbitrary object in the tree.
# ===================================================

"""
class Student:
    def __init__(self, number, name):
        self.grade = number  # this will serve as the object's key
        self.name = name

    def __lt__(self, kq):
        #FIXME: Write this function

    def __gt__(self, kq):
        return self.number > kq.number

    def __eq__(self, kq):
        #FIXME: Write this function

    def __str__(self):
        if self.grade is not None:
            #FIXME: Write this function

        # singly linked
        #         Returns a human readable string of the list content of the form
        #         [value1 -> value2 -> value3]
        #
        #         An empty list should just return []
        #
        #         Returns:
        #             The string of the human readable list representation
        #
        # out = '['
        # if self.head.next != self.tail:
        #     cur = self.head.next.next
        #     out = out + str(self.head.next.data)
        #     while cur != self.tail:
        #         out = out + ' -> ' + str(cur.data)
        #         cur = cur.next
        # out = out + ']'
        # return out
        #
        #
        # doubly linked
        # Returns a human readable string of the list content of the form
        # [value1 <-> value2 <-> value3]
        #
        # An empty list should just print []
        #
        # Returns:
        #     The string of the human readable list representation
        #
        # out = '['
        # if self.sentinel.prev != self.sentinel:
        #     cur = self.sentinel.next.next
        #     out = out + str(self.sentinel.next.data)
        #     while cur != self.sentinel:
        #         out = out + ' <-> ' + str(cur.data)
        #         cur = cur.next
        # out = out + ']'
        # return out
"""
class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val  # when this is a primitive, this serves as the node's key


class BST:
    def __init__(self, start_tree=None) -> None:
        """ Initialize empty tree """
        self.root = None

        # populate tree with initial nodes (if provided)
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self):
        """
        Traverses the tree using "in-order" traversal
        and returns content of tree nodes as a text string
        """
        values = [str(_) for _ in self.in_order_traversal()]
        return "TREE in order { " + ", ".join(values) + " }"

    def add(self, val):
        """
        Creates and adds a new node to the BSTree.
        If the BSTree is empty, the new node should added as the root.

        Args:
            val: Item to be stored in the new node
        """
        new_node = TreeNode(val)  # initialize a new link
        #if it is a primitive the value will be the key
        new_node.val = val  # set new_link val equal to value

        # if the tree is empty but for the sentinel
        if self.root == None:
            self.root = new_node #set the new node equal to root
            new_node.left = None
            new_node.right = None

        else:
            parent = None
            current_node = self.root

            while current_node is not None:
                parent = current_node
                if new_node.val <= current_node.val:
                    current_node = current_node.left
                else:
                    current_node = current_node.right
            if parent.val >= new_node.val:
                parent.left = new_node
            else:
                parent.right = new_node


    def in_order_traversal(self, cur_node=None, visited=None) -> []:
            """
            Perform in-order traversal of the tree and return a list of visited nodes
            """
            if visited is None:
                # first call to the function -> create container to store list of visited nodes
                # and initiate recursive calls starting with the root node
                visited = []
                self.in_order_traversal(self.root, visited)

            # not a first call to the function
            # base case - reached the end of current subtree -> backtrack
            if cur_node is None:
                return visited

            # recursive case -> sequence of steps for in-order traversal:
            # visit left subtree, store current node value, visit right subtree
            self.in_order_traversal(cur_node.left, visited)
            visited.append(cur_node.val)
            self.in_order_traversal(cur_node.right, visited)
            return visited

    def pre_order_traversal(self, cur_node=None, visited=None) -> []:
        """
        Perform pre-order traversal of the tree and return a list of visited nodes

        Returns:
            A list of nodes in the specified ordering
        """
        # FIXME: Write this function

    def post_order_traversal(self, cur_node=None, visited=None) -> []:
        """
        Perform post-order traversal of the tree and return a list of visited nodes

        Returns:
            A list of nodes in the specified ordering
        """
        # FIXME: Write this function

    def contains(self, kq):
        """
        Searches BSTree to determine if the query key (kq) is in the BSTree.

        Args:
            kq: query key

        Returns:
            True if kq is in the tree, otherwise False
        """
        if self.root == None:
            return False
        else:
            current_node = self.root
            while current_node is not None:
                if current_node.val == kq:
                    return True
                elif kq < current_node.val:
                    current_node = current_node.left
                elif kq > current_node.val:
                    current_node = current_node.right
            return False

    def left_child(self, node):
        """
        Returns the left-most child in a subtree.

        Args:
            node: the root node of the subtree

        Returns:
            The left-most node of the given subtree
        """
        #TODO: Need to test this helper function for remove
        node_to_remove = node
        right_child = node_to_remove.right
        left_child = node_to_remove.left
        sucessor_node = right_child

        # and then find the right subtrees left most node
        while sucessor_node.left is not None:
            #print(sucessor_node.val, "pre loop")
            #sucessor_parent = sucessor_node
            sucessor_node = sucessor_node.left
            #print(sucessor_node.val, "post loop")
        return sucessor_node

        # root = node
        # current_node = root
        #
        # while current_node.left is not None:
        #     current_node = current_node.left
        # return current_node.left.val


    def remove(self, kq):
        """
        Removes node with key k, if the node exists in the BSTree.

        Args:
            node: root of Binary Search Tree
            kq: key of node to remove

        Returns:
            True if k is in the tree and successfully removed, otherwise False
        """
        #no nodes in the tree
        if self.root == None:
            return False
        else:
            #have to find the node to remove if it exists in the tree
            current_node = self.root
            parent_node = current_node
            while current_node is not None:
                #print(current_node.val, "in loop")
                if kq < current_node.val:
                    parent_node = current_node
                    current_node = current_node.left
                elif kq > current_node.val:
                    parent_node = current_node
                    current_node = current_node.right
                elif current_node.val == kq:
                    node_to_remove = current_node
                    break

            # #if the node is not found it will return false
            # #otherwise now have the node_to_remove and parent_node (of the
            # #node to remove)
            # print(node_to_remove.val, "out of loop to remove")
            # print(parent_node.val, "out of loop parent")
            if current_node is None:
                return False
            else:
                #node to remove has no children
                if node_to_remove.left is None and node_to_remove.right is None:
                    #this may need to be just .left.val or without the value???
                    if parent_node.left == node_to_remove:
                        parent_node.left = None
                        # # free up N
                        # node_to_remove.val = None
                        # node_to_remove.left = None
                        # node_to_remove.right = None
                        return True
                    elif parent_node.right == node_to_remove:
                        parent_node.right = None
                        # # free up N
                        # node_to_remove.val = None
                        # node_to_remove.left = None
                        # node_to_remove.right = None
                        return True
                #node to remove has one right child
                elif node_to_remove.left is None and node_to_remove.right is not None:
                    #print(parent_node.val, "right child only")
                    if parent_node.left == node_to_remove:
                        parent_node.left = node_to_remove.right
                        return True
                    elif parent_node.right == node_to_remove:
                        parent_node.right = node_to_remove.right
                        return True
                #node to remove has one left child
                elif node_to_remove.right is None and node_to_remove.left is not None:
                    #print(parent_node.val, "left child only")
                    if parent_node.left == node_to_remove:
                        parent_node.left = node_to_remove.left
                        return True
                    elif parent_node.right == node_to_remove:
                        parent_node.right = node_to_remove.left
                        return True

                #now the node_to_remove is found, its parent is found
                #and we know the node has both a left and a right child
                else:
                    #move to the right child
                    right_child = node_to_remove.right
                    left_child = node_to_remove.left
                    sucessor_node = right_child
                    print("two children found")
                    print(node_to_remove.val, "to remove")
                    print(parent_node.val, "parent")
                    print(right_child.val, "right child")
                    print(left_child.val, "left child")
                    print(sucessor_node.val, "right child and current successor")

                    #and then find the right subtrees left most node
                    while sucessor_node.left is not None:
                        print(sucessor_node.val, "pre loop")
                        sucessor_parent = sucessor_node
                        sucessor_node = sucessor_node.left
                        print(sucessor_node.val, "post loop")

                    #exited loop
                    print(sucessor_node.val, "sucessor")
                    print(sucessor_parent.val, "sucessor parent")

                    #node to remove's right child is sucessor----
                    #that is that the node_to_remove's right child has no left
                    #child----this may need to be moved up one block
                    if sucessor_node == node_to_remove.right:
                        #update the parent node's new child to successor
                        if parent_node.left == node_to_remove:
                            parent_node.left = sucessor_node
                            #return True
                        elif parent_node.right == node_to_remove:
                            parent_node.right = sucessor_node
                            #return True
                    else:
                        print("you are here")
                        #fix the sucessor's new child and sucessor's parent's
                        #new child
                        sucessor_parent.left = sucessor_node.right
                        sucessor_node.right = node_to_remove.right

                        #update the parent node
                        if parent_node.left == node_to_remove:
                            parent_node.left = sucessor_node
                            #return True
                        elif parent_node.right == node_to_remove:
                            parent_node.right = sucessor_node
                            #return True

            #returns False if element is not found
            return False




    def get_first(self):
        """
        Gets the val of the root node in the BSTree.

        Returns:
            val of the root node, return None if BSTree is empty
        """
        if self.root == None:
            return None
        else:
            return self.root.val

    def remove_first(self):
        """
        Removes the val of the root node in the BSTree.

        Returns:
            True if the root was removed, otherwise False
        """
        #empty tree
        if self.root == None:
            return False
        else:
            #only a root node
            if self.root.right == None and self.root.left == None:
                self.root = None
                return True
            #only a left node
            elif self.root.right == None:
                new_root = self.root.right
                self.root = new_root
            else:
                new_root = self.root.right.val
                new_root.left.val = self.root.left


# #testing the add node function 1
# tree = BST()
# print(tree)
# tree.add(10)
# tree.add(15)
# tree.add(5)
# print(tree)
# tree.add(15)
# tree.add(15)
# print(tree)
# tree.add(5)
# print(tree)

# #testing the add node function 2
# tree2 = BST()
# tree2.add(10)
# tree2.add(10)
# print(tree2)
# tree2.add(-1)
# print(tree2)
# tree2.add(5)
# print(tree2)
# tree2.add(-1)
# print(tree2)

# #testing contains
# tree3 = BST()
# print(tree3.contains(0))
#
# tree4 = BST([10, 5, 15])
# print(tree4)
# #print(tree4.contains(10))
# print(tree4.contains(15))
# print(tree4.contains(-10))
# print(tree4.contains(5))


# #remove function PASSING
# tree6 = BST([10, 5, 15])
# print(tree6)
# print(tree6.remove(7))
# print(tree6)
# print(tree6.remove(15))
# print(tree6)
# print(tree6.remove(15))
# print(tree6)

# # remove function 2 PASSING
# tree7 = BST([10, 20, 5, 15, 17, 7, 12])
# print(tree7)
# #print(tree7.contains(10))
# print(tree7.remove(10))
# print(tree7)

#remove from video lecture
tree8 = BST([15, 10, 20, 18, 25, 23, 21, 24, 22, 30])
print(tree8)
print(tree8.remove(20))
print(tree8)









# #testing remove first
# tree5 = BST()
# print(tree5.get_first())
# tree5.add(10)
# tree5.add(15)
# tree5.add(5)
# print(tree5.get_first())
# print(tree5)