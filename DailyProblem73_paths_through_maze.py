"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

A maze is a matrix where each cell can either be a 0 or 1. A 0 represents that the cell is empty, and a 1 represents a wall that cannot be walked through. 
You can also only travel either right or down.

Given a nxm matrix, find the number of ways someone can go from the top left corner to the bottom right corner. You can assume the two corners will always be 0.

Example:
Input: [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
# 0 1 0
# 0 0 1
# 0 0 0
Output: 2
The two paths that can only be taken in the above example are: down -> right -> down -> right, and down -> down -> right -> right.

Here's some starter code:

def paths_through_maze(maze):
  # Fill this in.

print(paths_through_maze([[0, 1, 0],
                          [0, 0, 1],
                          [0, 0, 0]]))
# 2
"""
def paths_through_maze(maze):
    if len(maze) == 0 or len(maze[0]) == 0:
        return 0
    return dfs(maze, 0, 0)

def dfs(maze, r, c):
    if r == len(maze)-1 and c == len(maze[0])-1:
        return 1

    res = 0
    pos = [[0, 1], [1, 0]]
    for dr, dc in pos:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) \
                and maze[nr][nc] == 0:
            maze[nr][nc] = 1
            res += dfs(maze, nr, nc)
            maze[nr][nc] = 0

    return res

print(paths_through_maze([[0, 1, 0],
                          [0, 0, 1],
                          [0, 0, 0]]))
# 2