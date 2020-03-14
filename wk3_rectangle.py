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


rec_list = [Rectangle(1, 2), Rectangle(5, 6), Rectangle(3, 4), Rectangle(8, 1)]

print(rec_list)

# sort the rectangle according to the area
rec_list.sort(key=Rectangle.rec_area) # sort based on one attribute!!!IMPORTANT!
# print the sorted rectangle
print(rec_list)

rec_list.sort(key=lambda a: a.length) # sort based on width!!!USE of lambda!
# print the sorted rectangle
print(rec_list)



"""
rec = Rectangle(1, 2)
print(rec.rec_area())
print(rec.rec_perimeter())
"""