"""
Leetcode 20. Valid Parentheses
Easy--Dictionary, stack

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""
def isValid(s):
	bra_dic = {'(':')','[':']','{':'}'}
	lis = []
	
	for i in range(len(s)):
		if s[i] in bra_dic:
			lis.append(s[i])
		elif len(lis) != 0 and s[i] == bra_dic.get(lis[-1]):
			lis.pop()
		else:
			return False
	if len(lis) > 0:
		return False
	return True

inp = "()"
print(isValid(inp))
inp = "()[]{}"
print(isValid(inp))
inp = "("
print(isValid(inp))
inp = "]"
print(isValid(inp))
inp = "([)]"
print(isValid(inp))
inp = "{[]}"
print(isValid(inp))
