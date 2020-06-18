"""
1047. Remove All Adjacent Duplicates In String
Easy: Stack, ''.join(s_stack)

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

 

Example 1:

Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
"""
class Solution:
    def removeDuplicates(self, S: str) -> str:
        s_stack = [S[0]]
        for i in range(1, len(S)):
            if len(s_stack) != 0 and S[i] == s_stack[-1]:
                s_stack.pop()
            else:
                s_stack.append(S[i])
        
        return ''.join(s_stack)