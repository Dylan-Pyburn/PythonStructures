class Node:

    def __init__(self, next_node=None, prev_node=None, value=None):
        self.prev_node = prev_node
        self.next_node = next_node
        self.value = value

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def get_prev(self):
        return self.prev_node

    def set_prev(self, new_prev):
        self.prev_node = new_prev


class DoublyLinkedList:

    # CONSTRUCTOR
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.current = None

    # insert node to the front of the list
    def add_front(self, value):
        new_node = Node(value=value)

        # first node
        if self.head is None:
            self.head = self.tail = self.current = new_node

        # add to beginning
        else:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node

    # insert node to the rear of the list
    def add_rear(self, value):
        new_node = Node(value=value)

        # first node in list
        if self.tail is None:
            self.head = self.tail = self.current = new_node

        # add to end
        else:
            new_node.set_prev(self.tail)
            self.tail.set_next(new_node)
            self.tail = new_node

    # insert node directly before a given node
    # raise ValueError if given value is not found
    def insert_before(self, new_value, given_value):
        # empty list
        if self.head is None:
            raise ValueError('LinkedList is empty')
            return

        new_node = Node(new_value)
        curr = self.head

        # traverse to find the given node
        while curr.get_value() != given_value:
            curr = curr.get_next()

        # check that the given node was found
        if curr is None:
            raise ValueError(f'{given_value} not in LinkedList')
            return

        # given node found, insert new node
        if curr == self.head:
            self.add_front(new_value)
        else:
            new_node.set_prev(curr.get_prev())
            new_node.get_prev().set_next(new_node)
            new_node.set_next(curr)
            curr.set_prev(new_node)

    # insert node directly after a given node
    # raise ValueError if given value is not found
    def insert_after(self, new_value, given_value):
        # empty list
        if self.head is None:
            raise ValueError('LinkedList is empty')
            return

        new_node = Node(new_value)
        curr = self.head

        # traverse to find the given node
        while curr.get_value() != given_value:
            curr = curr.get_next()

        # check that the given node was found
        if curr is None:
            raise ValueError(f'{given_value} not in LinkedList')
            return

        # given node found, insert new node
        if curr == self.tail:
            self.add_rear(new_value)
        else:
            new_node.set_next(curr.get_next())
            new_node.get_next().set_prev(new_node)
            new_node.set_prev(curr)
            curr.set_next(new_node)

    # delete a node of a given value
    def remove(self, value):
        # empty list
        if self.head is None:
            raise ValueError('LinkedList is empty')
            return

        # traverse to find the given node
        while curr.get_value() != value:
            curr = curr.get_next()

        # check that the given value was found
        if curr is None:
            raise ValueError(f'{value} not in LinkedList')
            return

        # remove the node

        # check if node is head
        if curr.get_prev() is not None:
            curr.get_prev.set_next(curr.get_next())
        else:
            self.head = curr.get_next()

        # check if node is tail
        if curr.get_next() is not None:
            curr.get_next.set_prev(curr.get_prev())
        else:
            self.tail = curr.get_prev()

    # search for a value in the list
    def search(self, value):
        curr = self.head
        while curr:
            if curr.get_value() == value: return curr
            curr = curr.get_next()

        return None

    # return the length of the list
    def length(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.get_next()
        return count

    # print the list front to back
    def print_forward(self, new_line='\n'):
        curr = self.head
        while curr:
            print(curr.get_value())
            curr = curr.get_next()

    # print the list back to front
    def print_backward(self, new_line='\n'):
        curr = self.tail
        while curr:
            print(curr.get_value())
            curr = curr.get_prev()

    # return the items in the LinkedList as a list
    def get_elements(self):
        items = []
        curr = self.head

        while curr:
            items.append(curr.get_value())
            curr = curr.get_next()
        return items

    """
    The following methods deal with the 'current' attribute
    """

    # return the value of the current node
    def get_current(self):
        return self.current.get_value()

    # move current to its next node
    def next(self):
        if self.current.get_next() is None:
            return
        self.current = self.current.get_next()

    # move current to its previous node
    def prev(self):
        if self.current.get_prev() is None:
            return
        self.current = self.current.get_prev()
