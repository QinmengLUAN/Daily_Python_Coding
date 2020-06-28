"""
78. Subsets
Medium: Array, backtracking

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution:
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) > 0:
            res.append([])
            res.append([nums[0]])
        for i in range(1,len(nums)):
            for j in range(len(res)):
                res.append(res[j] + [nums[i]])
        return res
    
    def subsets(self, nums):
        return self.helper(nums, 0, [])
        
    def helper(self, nums, idx, res):
        if idx == len(nums):
            return [[]]
        res = []
        sub_res = self.helper(nums, idx +1, res)
        for s in sub_res:
            res.append(s)
            res.append(s+[nums[idx]])
        return res