"""
1091. Shortest Path in Binary Matrix
Medium: BFS, classic

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

Example 1:
Input: [[0,1],[1,0]]
Output: 2

Example 2:
Input: [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        res = 0
        curr_layer = deque()
        curr_layer.append([0, 0])
        grid[0][0] = 1
        
        while len(curr_layer) > 0:
            # print(curr_layer)
            res += 1
            for _ in range(len(curr_layer)):
                node = curr_layer.popleft()
                if node[0] == len(grid) - 1 and node[1] == len(grid[0]) - 1:
                    return res

                next_layer = self.helper(grid, node)
                for item in next_layer:
                        i, j = item[0], item[1]
                        grid[i][j] = 1
                        curr_layer.append(item)
        return -1
        
    def helper(self, grid, item):
        next_layer = []
        i, j = item[0], item[1]
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1:
            return next_layer
        pos = [[i-1,j],[i+1,j],[i,j-1],[i,j+1],[i-1,j-1],[i-1,j+1],[i+1,j-1],[i+1,j+1]]
        for i,j in pos:
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                if grid[i][j] == 0:
                    next_layer.append([i,j])
        return next_layer