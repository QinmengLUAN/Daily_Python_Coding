# To understand object and data structure
# Example 1: https://www.w3schools.com/python/python_classes.asp
# Example 2: https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
# write an object MyList with many methods: MyList, append, pop, print, node

class MyNode:
	def __init__(self, value):
		self.value = value
		self.before = None
		self.next = None

class MyList:
	def __init__(self):
		self.head = None
		self.tail = None 

	def append(self, value):
		appended = MyNode(value)
		if self.head  == None:
			self.head = appended
			self.tail = appended
		else:
			curr_tail = self.tail
			appended.before = curr_tail
			curr_tail.next = appended
			self.tail = appended

	def print(self):
		curr_node = self.head
		while curr_node != None:
			print(curr_node.value)
			curr_node = curr_node.next
	
	def get(self, n):
		curr_node = self.head
		i = 0
		while i < n and curr_node != None:
			curr_node = curr_node.next
			i = i + 1
		if curr_node == None:
			return None
		else:
			return curr_node.value

lis = MyList()
lis.append(1)
lis.append(2)
lis.print()

print(lis.get(1))


