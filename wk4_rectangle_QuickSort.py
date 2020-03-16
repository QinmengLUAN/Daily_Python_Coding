# To understand object
# write an object Student with many methods: 
# student name, student id, student height, student weight, student GPA

class Rectangle:
	
	def __init__(self, width, length):
		self.width = width
		self.length = length

	def rec_area(self):
		rec_area = self.width * self.length
		return rec_area
		
	def rec_perimeter(self):
		rec_perimeter = 2 * (self.width + self.length)
		return rec_perimeter

	def rec_print(self):
		print([self.width, self.length])

	def __repr__(self):
		return "(" + str(self.width) + " - " + str(self.length) + ")"



"""
My sort function below_quick sort algorithm
"""
import random

def swap_helpler(ls, idx_a, idx_b):
	temp = ls[idx_a]
	ls[idx_a] = ls[idx_b]
	ls[idx_b] = temp

def adjust(ls, item_key, start_index, end_index):

	"""
	item_key(ls[i]) -> int
	"""

    # Check whether the input is qualified
	if not 0 <= start_index < end_index < len(ls): # Very important line!!!
		return
	pivot_index = random.choice(range(start_index, end_index + 1))
	print(pivot_index)

	# pivot_index = (start_index + end_index) // 2
	swap_helpler(ls, start_index, pivot_index)

	j = end_index
	i = start_index + 1

	while i < j:
		while item_key(ls[i]) < item_key(ls[start_index]) and i < j: # item_key(ls[i]) -> return a value for the comparison
			i += 1
		while item_key(ls[j]) > item_key(ls[start_index]) and i < j:
			j -= 1	
		if i != j:
			swap_helpler(ls, i, j)
	
	if item_key(ls[i]) < item_key(ls[start_index]):
		swap_helpler(ls, start_index, i)
		pivot_index = i
	else:
		swap_helpler(ls, start_index, i - 1)
		pivot_index = i - 1

	adjust(ls, item_key, start_index, pivot_index - 1)
	adjust(ls, item_key, pivot_index + 1, end_index)

def QuickSort(ls, item_key):
	adjust(ls, item_key, 0, len(ls) - 1)

"""
End of the code
"""
rec_list = [Rectangle(1, 2), Rectangle(5, 6), Rectangle(3, 4), Rectangle(8, 1)]
QuickSort(rec_list, Rectangle.rec_area)
print(rec_list)

QuickSort(rec_list, item_key = lambda a: a.length + a.width)
print(rec_list)
"""
# sort the rectangle according to the area
rec_list.sort(key=Rectangle.rec_area) # sort based on one attribute!!!IMPORTANT!
# print the sorted rectangle
print(rec_list)

rec_list.sort(key=lambda a: a.length) # sort based on width!!!USE of lambda!
# print the sorted rectangle
print(rec_list)
"""


"""
rec = Rectangle(1, 2)
print(rec.rec_area())
print(rec.rec_perimeter())
"""