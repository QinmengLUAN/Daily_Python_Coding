"""
72. Edit Distance
Hard: DP

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == None or word2 == None:
            return -1
        r, c = len(word1), len(word2)
        
        dp = [[0] * (c+1) for i in range(r+1)]
        
        # initialization
        for i in range(r + 1):
            dp[i][0] = i
        for j in range(c + 1):
            dp[0][j] = j
        
        # Transition function:
        # If word1[i] != word[j]:
            # f[i][j] = min(f1, f2, f3)
            # f1 = f[i][j-1] + 1
            # f2 = f[i-1][j] + 1
            # f3 = f[i-1][j-1] +1
        # If word1[i] == word[j]:
            # f[i][j] = f[i-1][j-1]
        
        # Table filling:
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    f1 = dp[i-1][j] + 1
                    f2 = dp[i][j-1] + 1
                    f3 = dp[i-1][j-1] + 1
                    dp[i][j] = min(f1, f2, f3)
        return dp[-1][-1]