
class Node():

	def __init__(self, next_node=None, value=None):
		self.next = next_node
		self.value = value

	def get_value(self):
		return self.value

	def set_next(self, new_next):
		self.next = new_next

	def get_next(self):
		return self.next

class SinglyLinkedList(object):

	# CONSTRUCTOR
	def __init__(self, head=None):
		self.head = head

	# insert a node to the front of the lsit
	def insert(self, value):
		new_node = Node(value=value)
		new_node.set_next(self.head)
		self.head = new_node

	# delete first node with specified value
	# from the list
	def remove(self, value):
		# no nodes in list
		if self.head is None: return
		
		# delete the top node in list
		if self.head.get_value() == value:
			self.head = self.head.get_next()
			return

		curr = self.head
		while curr.get_next():
			# node found
			if curr.get_next().get_value() == value:
				curr.set_next( curr.get_next().get_next() )
				return
			# not found
			curr = curr.get_next()

	# search for a node with a specified value
	def search(self, value):
		curr = self.head
		while curr:
			if curr.get_value() == value: return curr
			curr = curr.get_next()

		return None

	# print the contents of a list
	def print(self):
		curr = self.head
		while curr:
			print(curr.get_value())
			curr = curr.get_next()

	# return the length of the list
	def length(self):
		curr = self.head
		count = 0
		while curr:
			count += 1
			curr = curr.get_next()

		return count

	# return the items in the linked list as a list
	def get_elements(self):
		items = []
		curr = curr.head

		while curr:
			items.append(curr.get_value())
			curr = curr.get_next()
		return items

