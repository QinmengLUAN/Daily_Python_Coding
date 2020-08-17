"""
1219. Path with Maximum Gold
Medium: Backtracking

In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position you can walk one step to the left, right, up or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
"""
class Solution:
    def 1(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    ans = max(ans, self.helper((i,j), grid))
        return ans
    
    def helper(self, pos, grid):
        i, j = pos[0], pos[1]
        max_gold = 0         
        grid[i][j] = - grid[i][j]
        npos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for x, y in npos:
            if 0 <= i+x < len(grid) and 0 <= j+y < len(grid[0]):
                if grid[i+x][j+y] > 0:
                    max_gold = max(self.helper((i+x, j+y), grid), max_gold)
        grid[i][j] = abs(grid[i][j])
        return max_gold + grid[i][j]