import random

class Solution():
    def maze(self, n):
        l = 2*n + 1
        # Start point; end point
        S, E = (0,1), (-1, -2)
        maze = [["." for i in range(l)] for j in range(l)]

        for i in range(l):
            for j in range(l):
                if i % 2 == 0 or j % 2 == 0:
                    maze[i][j] = "#"

        maze[S[0]][S[1]] = "S"
        maze[E[0]][E[1]] = "E"

        for i in range(1, l-1):
            for j in range(1, l-1):
                if maze[i][j] == ".":
                    self.dfs_helper(i, j, maze)

        # for i in range(l):
        #     print(" ".join(maze[i]))
        return maze

    def dfs_helper(self, r, c, maze):
        maze[r][c] = " "
        next_pos = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 < r+dr < len(maze)-1 and 0 < c+dc < len(maze)-1 and maze[r+dr][c+dc] == "#":
                # print( 0< r+dr+dr < len(maze)-1 and 0 < c+dc+dc < len(maze)-1, maze[r+dr+dr][c+dc+dc])
                if 0 < r+dr+dr < len(maze)-1 and 0 < c+dc+dc < len(maze)-1 and maze[r+dr+dr][c+dc+dc] == ".":
                    next_pos.append((r+dr, c+dc))

        if len(next_pos) == 0:
            return
        random_int = random.randint(0, len(next_pos)-1)
        i,j = next_pos[random_int][0], next_pos[random_int][1]
        maze[i][j] = " "
        return self.dfs_helper(i, j, maze)

s = Solution()
maze = s.maze(7)
for i in range(len(maze)):
    print(" ".join(maze[i]))
