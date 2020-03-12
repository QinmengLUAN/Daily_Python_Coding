# To understand object and data structure

# write an object MyList with many methods: MyList, append, pop, print, node

class MyNode:
	def __init__(self, value):
		self.value = value
		self.prev_node = None
		self.next_node = None

class MyList:
	def __ini__(self):
		dummy = MyNode(-1)
		self.head_node = dummy
		self.tail_node = dummy
	def append(self, value):
		new_node = MyNode(value)
		self.tail_node.next_node = new_node
		self.new_node.prev_node = self.tail_node
		self.tail_node = new_node
	def print(self):
		curr_node = head_node.next_node
		while curr_node != tail_node:
			print(curr_node.value)
			curr_node = curr_node.next_node

l = MyList()
l.append(1)
l.append(2)
l.print()


