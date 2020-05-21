
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

class Stack:

	# CONSTRUCTOR
	def __init__(self, top=None):
		self.top = top

	# add an item to top of stack
	def push(self, value):
		new_node = Node(value=value)
		new_node.set_next(self.top)
		self.top = new_node

	# return the value at top of stack
	def peek(self):
		if not self.top:
			return None
		return self.top.get_value()

	# return the value at top of stack
	# and delete the top node
	def pop(self):
		if self.top:
			value = self.top.get_value()
			self.top = self.top.get_next()
			return value

	# print the contents of stack
	def print(self):
		curr = self.top
		while curr:
			print(curr.get_value())
			curr = curr.get_next()

	# return true if the stack contains atleast 1 item
	def is_empty(self):
		if self.top:
			return True
		return False
