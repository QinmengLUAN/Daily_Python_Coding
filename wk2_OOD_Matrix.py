# Object Oriented Design (OOD)
# First time to write OOD
# OOD is like a package (i.e. object) with different functions

# Task: write a matrix object with several functions
# Initial function: m = Matrix(n) -> write a n*n matrix with all zeros 
# m.set(1,2,3) -> set position (1,2) as 3
# m.get(1,2) -> get the value of position (1.2)
# m.print() -> customise how to print
# m.rotate() -> clockwise rotate the matrix
	# Clockwise rotate a n*n matrix by 90 degree
	# Method 2: rotate the swap until the last item
	# Strength: do not need to add space


class Matrix:
	def __init__(self, num):
		self.matrix = [[0] * num for i in range(num)]

	def __str__(self):
		return str(self.matrix)

	def __len__(self):
		return len(self.matrix) * len(self.matrix)

	def print(self):
		for i in range(len(self.matrix)):
			print(self.matrix[i])
	
	def set(self, m, n, new_value):
		self.matrix[m][n] = new_value

	def get(self, m, n):
		get_value = self.matrix[m][n]
		print(get_value)

	def rotate(self):
		pass
		"""
		n = len(rotate.matrix)
		for i in range((n + 1)//2):
			for j in range()
		"""



m = Matrix(4ß)
#res = m.set(1,2,3)
m.print()
m.set(1,2,3)
m.print()
m.get(1,2)
print(m)
print(len(m))
#m.rotate()