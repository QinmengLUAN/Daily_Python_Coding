"""
5. Longest Palindromic Substring
Medium: String, DP

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        # resT = [[False]*len_s for i in range(len_s)]
        dq = deque()
        res = str()
        
        for i in range(len_s):
            dq.append((i,i))
            res = s[i]
        
        for j in range(len_s):
            if j + 1 < len_s and s[j] == s[j + 1]:
                dq.append((j, j + 1))
                res = s[j:j + 1 + 1]
        while len(dq) > 0:
            m, n = dq.popleft()
            if m - 1 >= 0 and n + 1 < len_s and s[m - 1] == s[n + 1]:
                dq.append((m - 1, n + 1))
                res = s[m - 1: n + 1 + 1]
        return res