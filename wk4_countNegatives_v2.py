"""
Leetcode 1351. Count Negative Numbers in a Sorted Matrix

Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:

Input: grid = [[-1]]
Output: 1

"""
def countNegatives(inp):
	rows = len(inp)
	cols = len(inp[0])
	count = 0

	i = 0
	j = cols - 1

	while 0 <= i < rows:
		while 0 <= j < cols and inp[i][j] < 0:
			j -= 1 
		count = count + (cols - 1 - j)	
		i += 1

	return count


inp = [[4,3,2,-1],[3,2,1,-1],[-1,-1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives(inp))