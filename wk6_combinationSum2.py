"""
40. Combination Sum II
Medium: Backtracking
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""
class Solution:
    def combinationSum2(self, candidates, target):
    	curr = []
    	total = []
    	idx = 0
    	appeared = []
    	self.helper(sorted(candidates), target, curr, total, idx, appeared)
    	return total

    def helper(self, candidates, target, curr, total, idx, appeared):
    	if sum(curr) > target:
    		return
    	if sum(curr) == target:
    		if curr not in appeared:
    			appeared.append(curr.copy())
    			total.append(curr.copy())
    			return
    	if sum(curr) < target:
    		for i in range(idx,len(candidates)):
    			curr.append(candidates[i])
    			self.helper(candidates, target, curr, total, i + 1, appeared)
    			curr.pop()

candidates = [10,1,2,7,6,1,5]
target = 8    		
s = Solution()
print(s.combinationSum2(candidates, target))
