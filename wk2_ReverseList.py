# Reverse the list
# e.g. [1,2,3] -> [3,2,1]
# Use swap

def ReverseList(inp):
	len_inp = len(inp)

	for i in range(len_inp // 2):
		temp = inp[i]
		inp[i] = inp[- 1 - i]
		inp[- 1 - i] = temp
	return inp

# Validation

inp = [1,2,3,4,5]

print(ReverseList(inp))

