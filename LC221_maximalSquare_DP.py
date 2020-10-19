"""
221. Maximal Square
Medium: DP

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        
        dp = [[0] * len(matrix[0]) for i in range(len(matrix))]
        for k in range(len(matrix)):
            if dp[k][0] < int(matrix[k][0]):
                dp[k][0] = 1
        
        for k in range(len(matrix[0])):
            if dp[0][k] < int(matrix[0][k]):
                dp[0][k] = 1
        
        res = max(max(dp))
        # print(res)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = 1
                    dp[i][j] += min(dp[i-1][j], dp[i][j-1],dp[i-1][j-1])
                    if dp[i][j] > res:
                        res = dp[i][j]
        return res**2