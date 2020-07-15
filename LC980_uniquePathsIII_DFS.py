"""
980. Unique Paths III
Hard: DFS, Backtracking

On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
"""
# DFS solution, table
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        s, e = [], []
        steps = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    s = [i, j]
                elif grid[i][j] == 0:
                    steps += 1
        return self.helper(grid, s, steps) 
        
    def helper(self, grid, s, steps):
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        res, np = 0, []
        i, j = s[0], s[1]
        for x, y in dirs:
            nx, ny = i + x, j + y
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                np.append([nx, ny])

        for pos in np:
            ni, nj = pos[0], pos[1]
            if grid[ni][nj] == 2 and steps == 0:
                res += 1   
            elif grid[ni][nj] == 0:
                grid[ni][nj] = -2
                steps -= 1
                # print(grid)
                res += self.helper(grid, pos, steps)
                steps += 1
                grid[ni][nj] = 0
        return res


# First solution
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        s, obs, e = [], set(), []
        pp = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    s = [i, j]
                    pp.add((i,j))
                elif grid[i][j] == 2:
                    e = [i, j]
                elif grid[i][j] == -1:
                    obs.add((i, j))
        steps = len(grid) * len(grid[0]) - len(obs) - 2
        return self.helper(grid, s, pp, obs, e, steps) 
            
        
    def helper(self, grid, s, pp, obs, e, steps):
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        np = []
        res = 0
        i, j = s[0], s[1]
        for x, y in dirs:
            nx = i + x
            ny = j + y
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if (nx, ny) not in obs and (nx, ny) not in pp:
                        np.append([nx, ny])
        for pos in np:
            if pos == e and steps == 0:
                res += 1
            elif pos != e:
                ni, nj = pos[0], pos[1]
                pp.add((ni, nj))
                steps -= 1
                res += self.helper(grid, pos, pp, obs, e, steps)
                steps += 1
                pp.remove((ni, nj))
        return res