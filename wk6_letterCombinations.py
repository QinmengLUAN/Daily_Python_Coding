"""
17. Letter Combinations of a Phone Number
Medium: Backtracking, go-to-hell question
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the *telephone buttons*) is given below. 
Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.

2 - a, b, c
3 - d, e, f
4 - g, h, i
5 - j, k, l
6 - m, n, o
7 - p, q, r, s
8 - t, u, v
9 - w, x, y, z
"""
class Solution:
	def letterCombinations(self, digits):
		dic = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
		if len(digits) == 0:
			return []
		dig = int(digits)
		nums = []
		while dig != 0:
			nums.append(dig % 10)
			dig = dig // 10
		nums.reverse()

		curr_list = []
		total = []
		self.helper(nums, curr_list, total, dic, len(nums))
		return total

	def helper(self, nums, curr_list, total, dic, N):
		# print(curr_list)
		if len(curr_list) > N:
			return
		if len(curr_list) == N:
			total.append("".join(curr_list))
			return
		if len(curr_list) < N:
			curr_choices = dic[nums[0]]
			for item in curr_choices:
				curr_list.append(item)
				self.helper(nums[1:], curr_list, total, dic, N)
				curr_list.pop()

s = Solution()
print(s.letterCombinations('2356'))







