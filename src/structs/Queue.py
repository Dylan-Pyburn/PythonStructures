class Node:

    def __init__(self, next_node=None, value=None):
        self.next_node = next_node
        self.value = value

    def get_value(self):
        return self.value

    def set_next(self, new_next):
        self.next_node = new_next

    def get_next(self):
        return self.next_node


class Queue:

    # CONSTRUCTOR
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    # add an item to end of queue
    def enqueue(self, value):
        new_node = Node(value=value)

        # queue is empty
        if self.front is None:
            self.front = self.rear = new_node

        # add to end of queue
        else:
            self.rear.set_next(new_node)
            self.rear = new_node

    # remove item from front of queue
    # return its value
    def dequeue(self):
        # empty queue
        if self.front is None:
            return None

        # remove and return first value
        value = self.front.get_value()
        self.front = self.front.get_next()

        # if the last item was removed
        if self.front is None:
            self.rear = None

        return value

    # return the value of front queue
    def front(self):
        if self.front is None:
            return None
        return self.front.get_value()

    # return the value of end of queue
    def rear(self):
        if not self.rear:
            return None
        return self.rear.get_value()

    # print the items in the queue
    def print(self):
        curr = self.front
        while curr:
            print(curr.get_value())
            curr = curr.get_next()

    # return true if the queue contains
    # atleast 1 item
    def is_empty(self):
        if self.front:
            return True
        return False
