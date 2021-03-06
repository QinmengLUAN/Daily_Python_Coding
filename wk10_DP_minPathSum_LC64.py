"""
64. Minimum Path Sum
Medium: table filling, time complexity O(M*N), space complexity O(M*N)
Follow-up: return the shortest path
----------------------------------------------------------
Codition: check the path to right, bottom
Initial state: res[0][0] = grid[0][0]
Transition function: res[i][j] = min(res[i-1][j], res[i][j-1]) + grid[i][j]
----------------------------------------------------------
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
class Solution:
    def minPathSum(self, grid):
        res = [[0] * len(grid[0])] * len(grid) 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    res[0][0] = grid[0][0]
                elif i == 0 and j != 0:
                    res[i][j] = res[i][j-1] + grid[i][j]

                elif j == 0 and i != 0:
                    res[i][j] = res[i-1][j] + grid[i][j]

                else:
                    res[i][j] = min(res[i-1][j], res[i][j-1]) + grid[i][j]
        # print(res)
        return res[-1][-1]

      
    # Return the min Sum and shortest path    
    def minPathSum_withPath(self, grid: List[List[int]]) -> int:    
        res = [[[0] * 2 for _ in range(len(grid[0]))] for __ in range(len(grid))] 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    res[0][0][0] = grid[0][0]
                    
                elif i == 0 and j != 0:
                    res[i][j][0] = res[i][j-1][0] + grid[i][j]
                    res[i][j][1] = 'left'

                elif j == 0 and i != 0:
                    res[i][j][0] = res[i-1][j][0] + grid[i][j]
                    res[i][j][1] = 'up'
                else:
                    res[i][j][0] = min(res[i-1][j][0], res[i][j-1][0]) + grid[i][j]
                    if res[i-1][j][0] <= res[i][j-1][0]:
                        res[i][j][1] = 'up'
                    else:
                        res[i][j][1] = 'left'
        print(res)
        return res[-1][-1][0]  
s = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(s.minPathSum(grid))
