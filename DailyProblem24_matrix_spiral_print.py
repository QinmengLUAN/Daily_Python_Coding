"""
Hi, here's your problem today. This problem was recently asked by Amazon:

You are given a 2D array of integers. 
Print out the clockwise spiral traversal of the matrix.

Example:

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

The clockwise spiral traversal of this array is:

1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12

Here is a starting point:

def matrix_spiral_print(M):
  # Fill this in.

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
"""
def matrix_spiral_print(matrix):
    # Fill this in.
    if matrix == []:
        return []
    up, left = 0, 0
    down = len(matrix) - 1
    right = len(matrix[0]) - 1
    
    direct = 0  # 0: go right   1: go down  2: go left  3: go up
    res = []
    
    while len(matrix) * len(matrix[0]) != len(res):
        if direct == 0:
            for i in range(left, right+1):
                res.append(matrix[up][i])
            up += 1
        elif direct == 1:
            for i in range(up, down+1):
                res.append(matrix[i][right])
            right -= 1
        elif direct == 2:
            for i in range(right, left-1, -1):
                res.append(matrix[down][i])
            down -= 1
        elif direct == 3:
            for i in range(down, up-1, -1):
                res.append(matrix[i][left])
            left += 1
        if up > down or left > right:
            return res
        direct = (direct + 1) % 4
    return res
    
class Solution:
    def spiralOrder2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        Use transpose of matrix
        """
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            matrix = [*zip(*matrix)][::-1]
        return res


grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

print(matrix_spiral_print(grid))
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12