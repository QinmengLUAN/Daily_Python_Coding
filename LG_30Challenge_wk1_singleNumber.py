"""
30 days Leetcode Challenge
wk1: singleNumber, need tricks	
Leetcode136 hash table
Given a non-empty array of integers, every element appears twice except for one. 
Find that single one.

Note:
Your algorithm should have a linear runtime complexity.(bit manipulation) 
Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
"""
class Solution:
    def singleNumber(self, nums):
    	i = 0
    	while i < len(nums):
    		temp_poped = nums.pop(i)
    		if temp_poped not in nums:
    			return temp_poped
    		nums.insert(i, temp_poped)
    		i += 1
"""
# Another solution: use bit manipulation
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
"""

nums = [2,2,1]
s = Solution()
print(s.singleNumber(nums))
