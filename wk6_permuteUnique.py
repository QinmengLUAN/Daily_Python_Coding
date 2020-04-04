"""
47. Permutations II
Medium: Backtracking
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
class Solution:
    def permuteUnique(self, nums):
    	curr = []
    	total = []
    	appeared = set()
    	idx = set(range(len(nums)))
    	self.helper(nums, curr, total, appeared, idx)
    	return total

    def helper(self, nums, curr, total, appeared, idx):
    	if len(curr) > len(nums):
    		return
    	if len(curr) == len(nums):
    		if str(curr.copy()) not in appeared:
    			total.append(curr.copy())
    			appeared.add(str(curr.copy()))	
    		return
    	if len(curr) < len(nums):
    		for i in idx.copy():
    			curr.append(nums[i])
    			idx.remove(i)
    			self.helper(nums, curr, total, appeared, idx)
    			idx.add(i)
    			curr.pop()
nums = [1,1,2,2]
s = Solution()
print(s.permuteUnique(nums))