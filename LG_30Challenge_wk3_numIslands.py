"""
200. Number of Islands
Medium: Tree, DFS

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
class Solution:
    def numIslands(self, grid):
        dyed_number = 1
        if len(grid) == 0:
            return 0                

        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
               if grid[i][j] == "1":
                    dyed_number += 1
                    self.dye_helper(grid, i, j, dyed_number)
        # print(grid)
        return dyed_number - 1 

    # find neighbours: input a position --> find its neighbours
    def neighbours(self, grid, i, j):
        rows, cols = len(grid), len(grid[0])
        neighbours = []
        five_neighbours = [(i-1, j),(i+1, j), (i, j+1), (i, j-1)]
        for ni, nj in five_neighbours:
            if 0 <= ni < rows and 0 <= nj < cols:
                neighbours.append((ni, nj))
        return neighbours

    # dye number: input a position --> dye all connected numbers whose value is 1
    def dye_helper(self, grid, ni, nj, dyed_number):
        grid[ni][nj] = dyed_number
        for (ni,nj) in self.neighbours(grid, ni, nj): 
            if grid[ni][nj] == "1":
                self.dye_helper(grid, ni, nj, dyed_number)


grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

s = Solution()
print(s.numIslands(grid))
