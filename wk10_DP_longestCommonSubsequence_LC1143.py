"""
1143. Longest Common Subsequence
Medium: DP, table filling, recursion, time complexity N(MN), space complexity N(MN)

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
# Solution 1: DP, table filling, time/space complexity O(M*N)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 and not text2:
            return 0
        
        n, m = len(text1), len(text2)
        # state and initiation
        dp = [[0] * (m + 1) for i in range(n + 1)]
        
        # table filling, function
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
        return dp[n][m]

# Solution 2: DP, recursion + cache, time/space complexity N(MN)
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
