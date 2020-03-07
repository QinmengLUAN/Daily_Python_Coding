#Given an array of integers, 
#return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, 
#and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def TwoSum(inp, target):
	new_inp = sorted([(inp[idx],idx) for idx in range(len(inp))])

	j = len(inp) - 1
	i = 0
	
	while i != j:
		current = new_inp[i][0] + new_inp[j][0]
		if current == target:
			return [new_inp[i][1],new_inp[j][1]]
		elif current > target:
			j = j - 1
		else:
			i = i +1



inp = [2, 17, 11, 15]
target = 19
print(TwoSum(inp, target))