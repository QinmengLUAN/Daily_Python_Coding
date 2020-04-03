"""
46. Permutations
Medium: Backtracking, classic

Given a collection of distinct integers, 
return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution:
	def permute(self, nums):
		i_set = set(range(len(nums)))
		curr = []
		total = []
		self.helper(nums, i_set, curr, total)
		return total

	def helper(self, nums, i_set, curr, total):
		if len(curr) > len(nums):
			return
		if len(curr) == len(nums):
			total.append(curr.copy())
			return
		if len(curr) < len(nums):
			for item in list(i_set):
				curr.append(nums[item])
				i_set.remove(item)
				self.helper(nums, i_set, curr, total)
				i_set.add(item)
				curr.pop()

nums = [1,2,3]
s = Solution()
print(s.permute(nums))

