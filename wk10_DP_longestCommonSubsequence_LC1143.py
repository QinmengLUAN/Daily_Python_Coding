"""
1143. Longest Common Subsequence
Medium: DP, Recursion, time complexity N(MN), space complexity N(MN)

Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
"""
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        return self.helper(text1, text2, 0, 0, {})

    def helper(self, text1, text2, i, j, cache):
        if (i, j) in cache:
            return cache[(i, j)]

        if i == len(text1) or j == len(text2):
            return 0

        if text1[i] == text2[j]:
            res = self.helper(text1, text2, i+1, j+1, cache) + 1
        else:
            res = max(self.helper(text1, text2, i, j+1, cache),
                       self.helper(text1, text2, i+1, j, cache))

        cache[(i, j)] = res

        return res

text1 = "tttaceg"
text2 = "baced" 
s = Solution()
print(s.longestCommonSubsequence(text1, text2))