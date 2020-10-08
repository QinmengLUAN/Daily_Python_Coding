"""
1221. Split a String in Balanced Strings
Easy

707

467

Add to List

Share
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
Example 4:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'

Tips:
Loop from left to right maintaining a balance variable when it gets an L increase it by one otherwise decrease it by one.
Whenever the balance variable reaches zero then we increase the answer by one.
"""
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt, res = 0, 0
        if len(s) < 2:
            return 0
        
        for i in range(len(s)):
            if s[i] == "R":
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                res += 1
            
        return res