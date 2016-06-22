# NOTE: THIS FILE IS COMPLETE.
from song import *


class BTNode:
    '''A BTNode class.'''

    def __init__(self, v, p=None):
        '''(BTNode, object, BTNode) -> NoneType
        A new BTNode with value v, no left or right
        children and parent p. p is None by default.'''

        self.value = v
        self.left = None
        self.right = None
        self.parent = p
        self.ht = 1

    def __str__(self):
        '''(BTNode) -> str
        Return the string representation of self.
        This method is called by print() and str()'''

        return "{}".format(self.value)

    def __repr__(self):
        '''(BTNode) -> str
        Return the internal string representation of self.
        This method is called when a list of BTNodes is
        printed.'''

        return "BTNode: {}".format(self.value)

    def set_right(self, n):
        '''(BTNode, BTNode) -> NoneType
        Make n the right child of self.
        Make self the parent of n if n exists.
        Set bidirectional links correctly.'''

        self.right = n
        if n:
            n.parent = self

    def set_left(self, n):
        '''(BTNode, BTNode) -> NoneType
        Make n the left child of self.
        Make self the parent of n if n exists.
        Set bidirectional links correctly.'''

        self.left = n
        if n:
            n.parent = self

    def is_left_child(self):
        '''(BTNode) -> bool
        Return True iff self's parent exists and self
        is the left child of its parent.'''

        return self.parent and self.parent.left is self

    def is_right_child(self):
        '''(BTNode) -> bool
        Return True iff self's parent exists and self
        is the right child of its parent.'''

        return self.parent and self.parent.right is self

    def is_leaf(self):
        '''(BTNode) -> bool
        Return True iff self is a leaf node.'''

        return not self.left and not self.right

    def height(self):
        '''(BTNode) -> int
        Return the height of self. Height is defined as the length of the
        longest path by number of nodes from self to a leaf.
        The height of a leaf node is 1.'''

        return self.ht

    def depth(self):
        '''(BTNode) -> int
        Return the depth of self. Depth is defined as the length of the
        path by number of nodes from the root of the tree to self.
        The depth of a root node is 1.'''

        if not self.parent:
            return 1
        return self.parent.depth() + 1

    def shallow_new_height(self):
        '''(BTNode) -> NoneType
        Recalculate the height of self given the heights
        of its left and right children. Do not recurse.
        Precondition: left and right child hights have been updated.'''

        left = 0
        right = 0
        if self.left:
            left = self.left.ht
        if self.right:
            right = self.right.ht
        self.ht = max(left, right) + 1

    def deep_new_height(self):
        '''(BTNode) -> NoneType
        Recursively calculate the height of self given the heights
        of its left and right subtrees.'''

        if not self:
            return 0
        left = 0
        right = 0
        if self.left:
            left = self.left.deep_new_height()
        if self.right:
            right = self.right.deep_new_height()
        self.ht = max(left, right) + 1
        return self.ht

    def update_heights(self):
        '''(BTNode) -> NoneType
        Recalculate self's height by recalculating heights of subtrees.
        Update the height of every ancestor BTNode above node.'''

        self.deep_new_height()
        p = self.parent
        while p:
            p.shallow_new_height()
            p = p.parent


class BSTree:
    '''A Binary Search Tree that conforms to the BST property at every step.
    The BST property states that for every node with value k, its left child
    is a (possibly empty) BST with values strictly less than k and its right
    child is a (possibly empty) BST with values strictly greater than k.'''

    def __init__(self, root=None):
        '''(BSTree, BTNode) -> NoneType
        Create a new BST with an optional root.'''

        self.root = root

    def print_tree(self):
        '''(BSTree) -> NoneType
        Print tree recursively (used for testing purposes)'''

        _print_tree(self.root, 1)

    def insert(self, n):
        '''(BSTree, BTNode) -> NoneType
        Insert new BTNode n into self. Do not duplicate values.
        Precondition: n's type is BTNode or a subclass.'''

        if not self.root:
            self.root = n
        _insert(self.root, n)

    def height(self):
        '''(BSTree) -> int
        Return the height of this tree.'''

        if self.root:
            return self.root.height()
        return 0

    def search(self, v):
        '''(BSTree, object) -> BTNode
        Return BTNode with value v if it exists in the tree. Return None
        if no such node exists. Assume unique node values.'''

        return _search(self.root, v)

    def range(self, v_start, v_end):
        '''(BSTree, object, object) -> list
        Return a list of Node objects with values between v_start and
        v_end inclusive. Assume v_start and v_end can be ordered and
        v_start <= v_end. v_start and v_end may not be values that
        exist in the tree.'''

        return _range(self.root, v_start, v_end)

    def delete(self, v):
        '''(BSTree, object) -> NoneType
        Delete node with value v from self. Change root if required.'''

        self.root = _delete(self.root, v)

    def starts_with(self, st):
        '''(BSTree, str) -> list
        Return all Pairs whose keys start with st.
        Precondition: self contains Pairs as node values'''

        startpair = Pair(st, None)
        endpair = Pair(st + "~", None)
        return self.range(startpair, endpair)


def _print_tree(root, depth):
    '''(BTNode, int) -> NoneType
    Print the left subtree of root, print root preceded by four spaces for
    every unit of depth, then print the right subtree of root.
    depth is the depth of root.'''

    if root is None:
        return
    _print_tree(root.right, depth + 1)
    print("    " * (depth - 1) + str(root))
    _print_tree(root.left, depth + 1)


def _insert(root, n):
    '''(BTNode, BTNode) -> BTNode
    Insert a new node n into BST rooted at root.
    Disregard equal values.'''

    if root.value == n.value:
        return
    if n.value < root.value:
        if root.left:
            _insert(root.left, n)
        else:
            root.set_left(n)
            n.update_heights()
    else:
        if root.right:
            _insert(root.right, n)
        else:
            root.set_right(n)
            n.update_heights()


def _search(root, v):
    '''(BTNode, object) -> BTNode
    Return BTNode with value v if it exists in subtree rooted at
    root. Return None if no such BTNode exists.'''

    if root is None:
        return None
    if root.value == v:
        return root
    elif v < root.value:
        return _search(root.left, v)
    elif v > root.value:
        return _search(root.right, v)


def _range(root, v_start, v_end):
    '''(BTNode, int, int) -> list
    Return an in-order list of BTNodes that have values between
    v_start and v_end, inclusive in subtree rooted at root.'''

    L = []
    if not root:
        return []
    if root.value > v_end:
        return _range(root.left, v_start, v_end)
    elif root.value < v_start:
        return _range(root.right, v_start, v_end)
    else:
        L.extend(_range(root.left, v_start, v_end))
        L.append(root)
        L.extend(_range(root.right, v_start, v_end))
        return L


def _delete(root, v):
    '''(BTNode, object) -> NoneType
    Delete BTNode with value v from subtree rooted at root.
    Return root of subtree. Do nothing if value doesn't exist in subtree.'''

    if not root:
        return root
    if root.value == v:
        if root.is_leaf():
            return None
        elif root.left and root.right:
            if root.left.height() >= root.right.height():
                toreplace = in_order_predecessor(root)
                root.value = toreplace.value
                root.set_left(_delete(root.left, toreplace.value))
            else:
                toreplace = in_order_successor(root)
                root.value = toreplace.value
                root.set_right(_delete(root.right, toreplace.value))
            return root
        elif root.left:
            return root.left
        elif root.right:
            return root.right
    elif root.value < v and root.right:
        root.set_right(_delete(root.right, v))
    elif root.value > v and root.left:
        root.set_left(_delete(root.left, v))
    return root


def in_order_predecessor(node):
    '''(BTNode) -> BTNode
    Return the in-order predecessor of node.
    Return None if node is leftmost.'''

    if node.left:
        curr = node.left
        while curr.right:
            curr = curr.right
        return curr
    else:
        curr = node
        while curr and not curr.is_right_child():
            if not curr.parent:
                return None
            curr = curr.parent
        return curr.parent


def in_order_successor(node):
    '''(BTNode) -> BTNode
    Return the in-order successor of node.
    Return None if node is rightmost.'''

    if node.right:
        curr = node.right
        while curr.left:
            curr = curr.left
        return curr
    else:
        curr = node
        while curr and not curr.is_left_child():
            if not curr.parent:
                return None
            curr = curr.parent
        return curr.parent


if __name__ == '__main__':
    bstree = BSTree()
    for val in [5, 7, 3, 2, 9, 8]:
        bstree.insert(BTNode(val))
    bstree.print_tree()
    print("=========")
