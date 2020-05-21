from structs.Tree import Tree, Node


class BinarySearchTree(Tree):
    """ Insert """

    # insert a node, recursive case
    # private
    def _insert(self, top_node, key):
        # insert location found
        if top_node is None:
            top_node = Node(key=key)

        # move left
        elif key < top_node.key:
            top_node.left = self._insert(top_node.left, key)

        # move right
        elif key > top_node.key:
            top_node.right = self._insert(top_node.right, key)

        return top_node

    """ Remove """

    # remove a node from the tree
    # the tree will still be a Binary search Tree
    def _remove(self, top_node, key):
        # move left
        if key < top_node.key:
            top_node.left = self._remove(top_node.left, key)

        # move right
        elif key > top_node.key:
            top_node.right = self._remove(top_node.right, key)

        # found
        else:
            # no children
            if not top_node.left and not top_node.right:
                return None

            # two children
            elif top_node.left and top_node.right:
                value = self._min_left(top_node)
                top_node.key = value
                top_node.right = self._remove(top_node.right, value)

            # one child
            else:
                if top_node.left: return top_node.left
                if top_node.right: return top_node.right

        return top_node
