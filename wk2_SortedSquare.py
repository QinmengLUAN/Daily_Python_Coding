# Square the values in the list, then sort it
# Example: [1, -2, 3] -> [1, 4, 9]
# Hint: time complexity O(N)

def Square(inp):
	new_list = []

	for i in range(len(inp)):
		new_list.append(inp[i] ** 2)
	return new_list

def Sorted(inp):
	sorted_new_list = []
	new_list = Square(inp)
	print(new_list)
	j = - 1
	i = 0
	while (-j + i) != len(inp):
		if new_list[i] < new_list[j]:
			sorted_new_list.append(new_list[j])
			j = j - 1
		else:
			sorted_new_list.append(new_list[i])
			i = i + 1

	sorted_new_list.reverse()
	return sorted_new_list

inp = [-6, -5, -3, -2 , -1, 0 , 1, 2, 5, 6, 6, 6]

print(Sorted(inp))