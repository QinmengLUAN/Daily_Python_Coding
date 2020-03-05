# Clockwise rotate a n*n matrix by 90 degree
# Method 2: rotate the swap until the last item
# Strength: do not need to add space

def rotateMatrix(matrix):
	m_len = len(matrix)
	for depth in range(m_len//2): #tuple check  tuple vs list
		init_pos = (depth,depth)
		inner_len = m_len - depth * 2

		for offset in range(inner_len - 1):

			leftup_pos = (init_pos[0], init_pos[1] + offset)
			rightup_pos = (init_pos[0] + offset, init_pos[1] + inner_len - 1)
			rightdown_pos = (init_pos[0] + inner_len - 1, init_pos[1] + inner_len - 1 - offset)
			leftdown_pos = (init_pos[0] + inner_len - 1 - offset, init_pos[1])

			#SWAP
			tmp = matrix[leftdown_pos[0]][leftdown_pos[1]]
			print(tmp)
			matrix[leftdown_pos[0]][leftdown_pos[1]]  = matrix[rightdown_pos[0]][rightdown_pos[1]] 
			matrix[rightdown_pos[0]][rightdown_pos[1]] = matrix[rightup_pos[0]][rightup_pos[1]]
			matrix[rightup_pos[0]][rightup_pos[1]] = matrix[leftup_pos[0]][leftup_pos[1]]
			matrix[leftup_pos[0]][leftup_pos[1]] = tmp

	return matrix


#Input: 
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(rotateMatrix(a))


#Testing
def generate_matrix(n):
  return [list(range(1 + i * n, 1 + i * n + n)) for i in range(n)]

def print_matrix(matrix):
  for row in matrix:
    print(row)

# Test below
# m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m = generate_matrix(9)
print_matrix(m)
rotate(m)
print("------------------------------")
print_matrix(m)