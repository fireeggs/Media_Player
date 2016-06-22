from bst import *


class AVLTree(BSTree):

    def insert(self, v):
        '''(AVLTree, object) -> NoneType
        Insert a new AVLNode with value v into self.
        Rebalance tree if required.'''

        BSTree.insert(self, AVLNode(v))
        return help_insert(AVLNode(v))

    def delete(self, v):
        '''(AVLTree, object) -> NoneType
        Do nothing and return nothing. Supersede BSTree.delete.
        NOTE: This method is complete.'''

        return None


def help_insert(avlNode):
    '''(object) -> NoneType.
    Insert a new AVLNode with value v into self.
    '''

    if avlNode != None:
        if avlNode.balance_factor() == 2:
        # check the balance factor of it's left child
            if avlNode.left.balance_factor() == 1:
            # as it is a LL case.
                right_rotate(avlNode.left)
                return avlNode.update_heights()
            elif avlNode.left.balance_factor() == -1:
            # as it is a LR case.
                left_rotate(avlNode.left)
                right_rotate(avlNode.left)
                return avlNode.update_heights()
        elif avlNode.balance_factor() == -2:
        # check the balance factor of it's right child
            if avlNode.right.balance_factor() == -1:
            # as it is a RR case.
                left_rotate(avlNode.right)
                return avlNode.update_height()
            elif avlNode.right.balance_factor() == 1:
            # as it is a RL case.
                right_rotate(avlNode.right)
                left_rotate(avlNode.right)
                return avlNode.update_height()
        elif avlNode.balance_factor in [-1, 0, 1]:
            return help_insert(avlNode.parent)
    return


class AVLNode(BTNode):

    def __repr__(self):
        '''(AVLNode) -> str
        Return the internal string representation of self.
        This method is called when a list of AVLNodes is
        printed.
        NOTE: This method is complete.'''

        return "AVLNode: {}".format(self.value)

    def balance_factor(self):
        '''(AVLNode) -> int
        Return the the height of self's left subtree minus the
        height of self's right subtree.'''

        if self.left == None and self.right == None:
        # as ABLNode has no left and right child.
            return 0
        elif self.left == None:
        # as ABLNode has no left child, but right child
            return - self.right.height
        elif self.right == None:
        # as ABLNode has no right child, but left child
            return self.left.height
        return self.left.height - self.right.height


def left_rotate(node):
    '''(BTNode) -> BTNode
    Perform a left rotation around node.
    Return the BTNode that now occupies the place of node in the tree.
    If node has no right child, do not alter tree and return node.'''

    if not node.right:
        return node
    else:  # as node has right child
        if node.parent:  # as node has parent
            if node.is_left_child():
                node.parent.left = node.right
                node.right.parent = node.parent
                return help_left_rotate(node)
            else:  # as node is right child of it's parent
                node.parent.right = node.right
                node.right.parent = node.parent
                return help_left_rotate(node)
        else:  # as node has no parent
            node.right.parent = None
            return help_left_rotate(node)


def help_left_rotate(node):
    '''(BTNode) -> BTNode
    Return node's right as the node that occupies the place of node
    '''

    if node.right.left:  # as node's right has left
        node.right.left.parent = node
        node_right_left = node.right.left
        node.right.left = node
        node.parent = node.right
        node_right = node.right
        node.right = node_right_left
        return node_right
    else:  # as node's right has no left
        node.right.left = node
        node.parent = node.right
        return node.right


def right_rotate(node):
    '''(BTNode) -> BTNode
    Perform a right rotation around node.
    Return the BTNode that now occupies the place of node in the tree.
    If node has no left child, do not alter tree and return node.'''

    if not node.left:
        return node
    else:  # as node has left child
        if node.parent:  # as node has parent
            if node.is_left_child():
                node.parent.left = node.left
                node.left.parent = node.parent
                return help_riht_rotate(node)
            else:  # as node is right child of it's parent
                node.parent.right = node.left
                node.left.parent = node.parent
                return help_right_rotate(node)
        else:  # as node has no parent
            node.left.parent = None
            return help_right_rotate(node)


def help_right_rotate(node):
    '''(BTNode) -> BTNode
    Return node's left as the node that occupies the place of node
    '''

    if node.left.right:  # as node's left has right
        node.left.right.parent = node
        node_left_right = node.left.right
        node.left.right = node
        node.parent = node.left
        node_left = node.left
        node.left = node_left_right
        return node_left
    else:  # as node's left has no right
        node.left.right = node
        node.parent = node.left
        return node.left

if __name__ == '__main__':

    tree = AVLTree()
    for i in [2, 1, 4, 3]:
        tree.insert(i)
    tree.print_tree()
    print("===========")
    # set the new root of the tree if needed!
    tree.root = left_rotate(tree.root)
    tree.print_tree()
    print("===========")
    tree.root = right_rotate(tree.root)
    tree.print_tree()
