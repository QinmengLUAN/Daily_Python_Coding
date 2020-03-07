#Given an array of integers, 
#return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, 
#and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def TwoSum(inp, target):
	
	for i in range(len(inp)):
		second_num = target - inp[i]

		for j in range(1,len(inp)):
			if inp[j] == second_num:
				return [i,j] 

inp = [2, 7, 11, 15]
target = 17
print(TwoSum(inp, target))