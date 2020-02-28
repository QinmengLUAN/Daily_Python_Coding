# Clockwise rotate a n*n matrix by 90 degree

# Method 1: give position[i][j] to [j][n-1-i]
# Drawback: waste space

def rotateMatrix(matrix):
	n = len(matrix)
	new_matrix = [[0]*n for i in range(n)]
	for i in range(n): # index of row
		for j in range(n): # index of column
			new_matrix[j][n-1-i] = matrix[i][j]
			print(i,j)
	return new_matrix


#Input: 
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(rotateMatrix(a))