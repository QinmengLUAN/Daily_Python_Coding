""" Insert Sort """

def insert_sort(i):
	"""todo"""

	for start in range(0,len(i)-1): 
		# select max for position(i)
		current_max = -1
		for index in range(start+1,len(i)):
			current_num = i[index]
			if current_num > current_max:
				current_max = current_num
				point = index
	#print(point)

		# swap		
		temp = i[start]
		i[start] = current_max
		i[point] = temp
	return i
	
	
	#new_list.pop = current_max





inp = [1,4,2,3,5,6]
for num in insert_sort(inp):
	print(num)
