"""
39. Combination Sum
Medium: Backtracking

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
class Solution:
    def combinationSum(self, candidates, target):
    	curr = []
    	total_combination = []
    	self.helper(candidates, target, curr, total_combination)

    	return total_combination
    def helper(self, candidates, target, curr, total_combination):
    	if sum(curr) > target:
    		return 
    	if sum(curr) == target:
    		total_combination.append(curr.copy())
    		return
    	if sum(curr) < target:
    		for item in list(candidates):
    			curr.append(item)
    			self.helper(candidates.copy(), target, curr, total_combination)
    			curr.pop()
    			candidates.remove(item)
candidates = [2,3,6,7]
target = 7
s = Solution()
print(s.combinationSum(candidates, target))    	  