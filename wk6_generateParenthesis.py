"""
Leetcode 22. Generate Parentheses
Medium: Backtracking, DFS application

Given n pairs of parentheses, 
write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
class Solution:
	def generateParenthesis(self, n):
		curr = []
		total = []
		self.helper(n, n, curr, total)
		return total

	def helper(self, n_left, n_right, curr, total):
		if n_left > n_right:
			return
		if n_left == n_right == 0:
			total.append("".join(curr))
			return 
		if n_left > 0:
			curr.append('(')
			self.helper(n_left - 1, n_right, curr, total)
			curr.pop()
		if n_right > 0:
			curr.append(')')
			self.helper(n_left, n_right - 1, curr, total)
			curr.pop()

s = Solution()
print(s.generateParenthesis(3))