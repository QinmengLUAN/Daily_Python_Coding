# Clockwise rotate a n*n matrix by 90 degree
# Method 2: rotate the swap until the last item
# Strength: do not need to add space

def rotateMatrix(matrix):
	n = len(matrix)
	for i in range((n + 1)//2):
		for j in range(n - 1):
			tmp = matrix[n - 1 - i][j]
			print(tmp)
			matrix[n - 1 - i][j] = matrix[n - 1- i][n - 1 - j]
			matrix[n - 1- i][n - 1 - j] = matrix[i][n - 1 - j]
			matrix[i][n - 1 - j] = matrix[i][j]
			matrix[i][j] = tmp

	return matrix


#Input: 
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(rotateMatrix(a))