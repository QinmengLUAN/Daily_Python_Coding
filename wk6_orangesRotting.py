"""
leetcode 994. Rotting Oranges
Easy: BFS, Moe feels this one is hard.

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
"""   	
class Solution(object):
	def orangesRotting(self, grid):
		rows, cols = len(grid), len(grid[0])
		rotted = set()
		not_rotted = set()
		times = 0
		total = 0
		for i in range(rows): # calculate total no of oranges
			for j in range(cols):
				if grid[i][j] != 0:
					total += 1
					if grid[i][j] == 2:
						rotted.add((i,j))
					elif grid[i][j] == 1:
						not_rotted.add((i,j))
		if total == 0:
			return 0
		while len(rotted) > 0:
			next_rotted = set()
			for (i, j) in rotted:
				for (a, b) in self.neighbours(i, j, rows, cols):
					if (a, b) in not_rotted:
						next_rotted.add((a, b))
						not_rotted.remove((a, b))
			rotted = next_rotted
			times += 1
		
		if len(not_rotted) != 0:
			return -1
		else:
			return times - 1


	def neighbours(self, i, j, rows, cols):
		neighbours = []
		four_neigh = [(i-1, j),(i+1, j), (i, j+1), (i, j-1)]
		for ni, nj in four_neigh:
			if 0 <= ni < rows and 0 <= nj < cols:
				neighbours.append((ni, nj))
		return neighbours

s = Solution()
inp = [[0]]
print(s.orangesRotting(inp))
