def remove(self, kq):
    """
    Removes node with key k, if the node exists in the BSTree.

    Args:
        node: root of Binary Search Tree
        kq: key of node to remove

    Returns:
        True if k is in the tree and successfully removed, otherwise False
    """
    # no nodes in the tree
    if self.root == None:
        return False
    else:
        # have to find the node to remove if it exists in the tree
        current_node = self.root
        parent_node = current_node
        node_to_remove = current_node
        while current_node is not None:
            # print(current_node.val, "in loop")
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
            # node to remove has no children
            if node_to_remove.left is None and node_to_remove.right is None:
                # this may need to be just .left.val or without the value???
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
            # node to remove has one right child
            elif node_to_remove.left is None and node_to_remove.right is not None:
                # print(parent_node.val, "right child only")
                if parent_node.left == node_to_remove:
                    parent_node.left = node_to_remove.right
                    return True
                elif parent_node.right == node_to_remove:
                    parent_node.right = node_to_remove.right
                    return True
            # node to remove has one left child
            elif node_to_remove.right is None and node_to_remove.left is not None:
                # print(parent_node.val, "left child only")
                if parent_node.left == node_to_remove:
                    parent_node.left = node_to_remove.left
                    return True
                elif parent_node.right == node_to_remove:
                    parent_node.right = node_to_remove.left
                    return True

            # now the node_to_remove is found, its parent is found
            # and we know the node has both a left and a right child
            else:
                # move to the right child
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
                # and then find the right subtrees left most node
                while sucessor_node.left is not None:
                    # print(sucessor_node.val, "pre loop")
                    sucessor_parent = sucessor_node
                    sucessor_node = sucessor_node.left
                    # print(sucessor_node.val, "post loop")

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
                    # node to remove's right child is sucessor----
                    # that is that the node_to_remove's right child has no left
                    # child----this may need to be moved up one block
                    if sucessor_node == node_to_remove.right:
                        # update the parent node's new child to successor
                        if parent_node.left == node_to_remove:
                            parent_node.left = sucessor_node
                            # return True
                        elif parent_node.right == node_to_remove:
                            parent_node.right = sucessor_node
                            # return True
                        # still need to account for the left child of the node to remove
                        sucessor_node.left = node_to_remove.left
                        return True
                    else:
                        # print("you are here")
                        # fix the sucessor's new child and sucessor's parent's
                        # new child
                        sucessor_parent.left = sucessor_node.right
                        sucessor_node.right = node_to_remove.right
                        sucessor_node.left = node_to_remove.left

                        # update the parent node
                        if parent_node.left == node_to_remove:
                            parent_node.left = sucessor_node
                            return True
                        elif parent_node.right == node_to_remove:
                            parent_node.right = sucessor_node
                            return True

        # returns False if element is not found
        return False