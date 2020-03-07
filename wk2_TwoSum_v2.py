#Given an array of integers, 
#return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, 
#and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def TwoSum(inp, target):
	inp.sort()	
	length = len(inp)
	j = length - 1
	i = 0

	while i != j:
		if (inp[i] + inp[j]) == target:
			return [inp[i],inp[j]]
		elif (inp[i] + inp[j]) > target:
			j = j - 1
		elif (inp[i] + inp[j]) < target:
			i = i +1



inp = [2, 17, 11, 15]
target = 19
print(TwoSum(inp, target))