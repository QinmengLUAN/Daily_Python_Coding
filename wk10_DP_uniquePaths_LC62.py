"""
62. Unique Paths
Medium: DP

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""
class Solution:
    def uniquePaths(self, m, n):
        res = [[0] * m for i in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    res[i][j] = 1
                else:
                    res[i][j] = res[i - 1][j] + res[i][j - 1]
        print(res)
        return res[n - 1][m - 1]


s = Solution()
m, n = 7, 2
print(s.uniquePaths(m, n))