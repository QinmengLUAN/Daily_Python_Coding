"""
784. Letter Case Permutation
Easy: Backtracking

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  
Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:
S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""
class Solution:
    def letterCasePermutation(self, S):
    	curr = []
    	total = []
    	N = len(S)
    	self.helper(S, curr, total, N)
    	return total
    def helper(self, S, curr, total, N):
    	if len(curr) > N:
    		return
    	if len(curr) == N:
    		total.append("".join(curr))
    		return
    	if len(curr) < N:
    		curr.append(S[0])
    		print(curr)
    		self.helper(S[1:], curr, total, N)
    		curr.pop()
    		if 'a' <= S[0] <= 'z':
    			curr.append(S[0].upper())
    			self.helper(S[1:], curr, total, N)
    			curr.pop()
    		if 'A' <= S[0] <= 'Z':
    			curr.append(S[0].lower())
    			self.helper(S[1:], curr, total, N)
    			curr.pop()
S = "a1b2"
s = Solution()
print(s.letterCasePermutation(S))
