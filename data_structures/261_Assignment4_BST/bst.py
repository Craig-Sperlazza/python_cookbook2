# bst.py
# ===================================================
# Implement a binary search tree that can store any
# arbitrary object in the tree.
# ===================================================


class Student:
    def __init__(self, number, name):
        self.grade = number  # this will serve as the object's key
        self.name = name

    def __lt__(self, kq):
        return self.grade < kq.grade

    def __gt__(self, kq):
        return self.grade > kq.grade

    def __eq__(self, kq):
        return self.grade == kq.grade

    def __str__(self):
        if self.grade is not None:
            return f'(Student:{self.name}, Grade:{self.grade})'

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
                if new_node.val < current_node.val:
                    current_node = current_node.left
                else:
                    current_node = current_node.right
            if parent.val > new_node.val:
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
        if visited is None:
            # first call to the function -> create container to store list of visited nodes
            # and initiate recursive calls starting with the root node
            visited = []
            self.pre_order_traversal(self.root, visited)

        # not a first call to the function
        # base case - reached the end of current subtree -> backtrack
        if cur_node is None:
            return visited

        # recursive case -> sequence of steps for pre-order traversal:
        # visit left subtree, visit right subtree, store current node value
        visited.append(cur_node.val)
        self.pre_order_traversal(cur_node.left, visited)
        self.pre_order_traversal(cur_node.right, visited)
        return visited

    def post_order_traversal(self, cur_node=None, visited=None) -> []:
        """
        Perform post-order traversal of the tree and return a list of visited nodes

        Returns:
            A list of nodes in the specified ordering
        """
        if visited is None:
            # first call to the function -> create container to store list of visited nodes
            # and initiate recursive calls starting with the root node
            visited = []
            self.post_order_traversal(self.root, visited)

        # not a first call to the function
        # base case - reached the end of current subtree -> backtrack
        if cur_node is None:
            return visited

        # recursive case -> sequence of steps for post-order traversal:
        # visit left subtree, visit right subtree, store current node value,
        self.post_order_traversal(cur_node.left, visited)
        self.post_order_traversal(cur_node.right, visited)
        visited.append(cur_node.val)
        return visited

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
        start_node = node
        right_child = start_node.right
        left_child = start_node.left

        if left_child is None:
            return start_node
        else:
            # and then find the right subtrees left most node
            while start_node.left is not None:
                start_node = start_node.left
                #print(sucessor_node.val, "post loop")
            return start_node



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
        #if we are removing the root node
        elif self.root.val == kq:
            if self.root.right == None and self.root.left == None:
                self.root = None
                return False
            #only a left node
            elif self.root.right == None:
                new_root = self.root.left
                self.root = new_root
                return True
            #only a right node
            elif self.root.left == None:
                new_root = self.root.right
                self.root = new_root
                return True
            #root has two children
            else:
                #start by getting right child
                right_child = self.root.right
                left_child = self.root.left
                #right child has no left subtree
                if right_child.left == None:
                    right_child.left = left_child
                    self.root = right_child
                    return True
                else:
                    sucessor_node = right_child
                    sucessor_parent = sucessor_node
                    # and then find the right subtrees left most node
                    while sucessor_node.left is not None:
                        # print(sucessor_node.val, "pre loop")
                        sucessor_parent = sucessor_node
                        sucessor_node = sucessor_node.left
                        # print(sucessor_node.val, "post loop")

                    # if node_to_remove == self.root:
                    sucessor_parent.left = sucessor_node.right
                    sucessor_node.right = self.root.right
                    sucessor_node.left = self.root.left
                    self.root = sucessor_node
                    return True
        else:
            #have to find the node to remove if it exists in the tree
            current_node = self.root
            parent_node = current_node
            node_to_remove = current_node
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
                    # print("two children found")
                    # print(node_to_remove.val, "to remove")
                    # print(parent_node.val, "parent")
                    # print(right_child.val, "right child")
                    # print(left_child.val, "left child")
                    # print(sucessor_node.val, "right child and current successor")

                    sucessor_parent = sucessor_node
                    #and then find the right subtrees left most node
                    while sucessor_node.left is not None:
                        #print(sucessor_node.val, "pre loop")
                        sucessor_parent = sucessor_node
                        sucessor_node = sucessor_node.left
                        #print(sucessor_node.val, "post loop")

                    # #exited loop
                    # print(sucessor_node.val, "sucessor")
                    # print(sucessor_parent.val, "sucessor parent")
                    # print(node_to_remove.val, "node to remove")
                    # print(parent_node.val, "node to remove parent")

                    if node_to_remove == self.root:
                        sucessor_parent.left = sucessor_node.right
                        sucessor_node.right = node_to_remove.right
                        sucessor_node.left = node_to_remove.left
                        self.root = sucessor_node
                    else:
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
                            #still need to account for the left child of the node to remove
                            sucessor_node.left = node_to_remove.left
                            return True
                        else:
                            #print("you are here")
                            #fix the sucessor's new child and sucessor's parent's
                            #new child
                            sucessor_parent.left = sucessor_node.right
                            sucessor_node.right = node_to_remove.right
                            sucessor_node.left = node_to_remove.left

                            #update the parent node
                            if parent_node.left == node_to_remove:
                                parent_node.left = sucessor_node
                                return True
                            elif parent_node.right == node_to_remove:
                                parent_node.right = sucessor_node
                                return True

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
                return False
            #only a left node
            elif self.root.right == None:
                new_root = self.root.left
                self.root = new_root
                return True
            #only a right node
            elif self.root.left == None:
                new_root = self.root.right
                self.root = new_root
                return True
            #root has two children
            else:
                #start by getting right child
                right_child = self.root.right
                left_child = self.root.left
                #right child has no left subtree
                if right_child.left == None:
                    right_child.left = left_child
                    self.root = right_child
                    return True
                else:
                    sucessor_node = right_child
                    sucessor_parent = sucessor_node
                    # and then find the right subtrees left most node
                    while sucessor_node.left is not None:
                        # print(sucessor_node.val, "pre loop")
                        sucessor_parent = sucessor_node
                        sucessor_node = sucessor_node.left
                        # print(sucessor_node.val, "post loop")

                    # if node_to_remove == self.root:
                    sucessor_parent.left = sucessor_node.right
                    sucessor_node.right = self.root.right
                    sucessor_node.left = self.root.left
                    self.root = sucessor_node
                    return True



# #remove first example 3
# tree = BST([10, 10, -1, 5, -1])
# print(tree.remove_first(), tree)
# print(tree.remove_first(), tree)
# print(tree.remove_first(), tree)
# print(tree.remove_first(), tree)
# print(tree.remove_first(), tree)
#


#
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
#
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
# print(tree7.remove(20))
# print(tree7)

# #remove from video lecture
# tree8 = BST([15, 10, 20, 18, 25, 23, 21, 24, 22, 30])
# print(tree8)
# print(tree8.remove(20))
# print(tree8)
# #
# test_values1 = [15, 0, -5, 5, 20, 25, 17]
# test_values2 = [Student(15, "Root"), Student(0, "Root->L"), Student(-5, "Root->L->L"),
#                        Student(5, "Root->L->R"), Student(20, "Root->R"), Student(25, "Root->R->R"),
#                        Student(17, "Root->R->L")]
# new_tree1 = BST(test_values1)
# print("in order")
# print(new_tree1.in_order_traversal())
# print("pre order")
# print(new_tree1.pre_order_traversal())
#
# new_tree1.remove(15)
# print("in order")
# print(new_tree1.in_order_traversal())
# print("pre order")
# print(new_tree1.pre_order_traversal())

# #testing remove first
# tree5 = BST()
# print(tree5.get_first())
# tree5.add(10)
# tree5.add(15)
# tree5.add(5)
# print(tree5.get_first())
# print(tree5)

##########################################################
# # Preorder Testing
# tree8 = BST([10, 20, 5, 15, 17, 7, 12])
# print(tree8.pre_order_traversal())
#
# tree9 = BST([10, 10, -1, 5, -1])
# print(tree9.pre_order_traversal())

# ##########################################################
# #post-order testing
# tree10 = BST([10, 20, 5, 15, 17, 7, 12])
# print(tree10.post_order_traversal())
#
# tree11 = BST([10, 10, -1, 5, -1])
# print(tree11.post_order_traversal())

# #homework Number 3
# tree11 = BST([40, 16, 50, 10, 19, 45, 92, 1, 15, 17, 35, 43, 47, 75, 101])
# print(tree11.in_order_traversal())
# tree11.remove(40)
# print(tree11.in_order_traversal())
# tree11.remove(16)
# print(tree11.in_order_traversal())