"""
1295. Find Numbers with Even Number of Digits
Given an array nums of integers, return how many of them contain an even number of digits.

Example 1:
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

Example 2:
Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
"""
def findNumbers(nums):
	oup = 0
	k = 0
	for i in range(len(nums)):
		nu = nums[i]
		while nu > 0:
			nu = nu // 10
			k += 1
		if (k % 2) == 0:
			oup += 1
		k = 0 
	return oup 

nums = [437,315,322,431,686,264,442]
print(findNumbers(nums))