from abc import ABC, abstractmethod


class Node:

    def __init__(self, left_child=None, right_child=None, key=None):
        self.left = left_child
        self.right = right_child
        self.key = key


class Tree(ABC):
    """ Constructor """

    def __init__(self, root=None):
        self.root = root

    """ Insert """

    def insert(self, key):
        # tree is empty
        if self.root is None:
            self.root = Node(key=key)

        # find insert location recursively
        else:
            self.root = self._insert(self.root, key)

    @abstractmethod
    def _insert(self, top_node, key):
        pass

    """ Search """

    # return the node with the specified key
    # or None if key is not in tree
    def search(self, key):
        if self.root:
            return self._search(self.root, key)
        else:
            print("Cannot search empty tree")

    def _search(self, top_node, key):
        # move left
        if key < top_node.key:
            return self._search(top_node.left, key)

        # move right
        elif key > top_node.key:
            return self._search(top_node.right, key)

        # node found
        else:
            return top_node

    """ Remove """

    def remove(self, key):
        # empty tree
        if not self.root:
            print("Cannot delete from empty tree")
            return

        # not in tree
        key_node = self.search(key)
        if not key_node:
            print(f"{key} not in tree")
            return

        else:
            self.root = self._remove(self.root, key)

    @abstractmethod
    def _remove(self, top_node, key):
        pass

    """ Printing """

    # ---- Infix -----------------
    def print_infix(self):
        if self.root:
            print(self._print_infix(self.root))
        else:
            print("Tree is empty")

    def _print_infix(self, top_node, tree_str=''):
        if top_node.left:
            tree_str = self._print_infix(top_node.left, tree_str)

        tree_str += str(top_node.key) + ' '

        if top_node.right:
            tree_str = self._print_infix(top_node.right, tree_str)

        return tree_str

    # ---- Prefix ----------------
    def print_prefix(self):
        if self.root:
            print(self._print_prefix(self.root))
        else:
            print("Tree is empty")

    def _print_prefix(self, top_node, tree_str=''):
        tree_str += str(top_node.key) + ' '

        if top_node.left:
            tree_str = self._print_prefix(top_node.left, tree_str)

        if top_node.right:
            tree_str = self._print_prefix(top_node.right, tree_str)

        return tree_str

    # ---- Postfix ---------------
    def print_postfix(self):
        if self.root:
            pass
        else:
            print("Tree is empty")

    def _print_postfix(self, top_node, tree_str=''):
        if top_node.left:
            tree_str = self._print_postfix(top_node.left, tree_str)

        if top_node.right:
            tree_str = self._print_postfix(top_node, tree_str)

        tree_str += str(top_node.key) + ' '

        return tree_str

    """ Utility """

    def _min_left(self, top_node):
        while top_node.left:
            top_node = top_node.left
        return top_node.key
