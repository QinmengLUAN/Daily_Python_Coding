"""
Hi, here's your problem today. This problem was recently asked by Uber:
Leetcode 20
Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using strings.

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

Example:
Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False
class Solution:
  def isValid(self, s):
    # Fill this in.

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
"""
class Solution:
  def isValid(self, s):
    # Fill this in.
    bra_dic = {")":"(", "}": "{", "]":"["}
    stack = []
    for i in range(len(s)):
        if s[i] not in bra_dic:
            stack.append(s[i])
        else:
            if len(stack) == 0 or stack[-1] != bra_dic[s[i]]:
                return False
            else:
                stack.pop()
    if len(stack) > 0:
        return False
    else:
        return True

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))