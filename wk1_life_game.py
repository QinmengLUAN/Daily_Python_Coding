def next_state(board):
	len_x = len(board)
	len_y = len(board[0])

	board_matrix = [[0]*(len_y+2) for i in range(len_x + 2)]
	label_matrix = [[0]*(len_y) for i in range(len_x)]


	for i in range(len_x):
		for j in range(len_y):
			board_matrix[i + 1][j + 1] = board[i][j]



	for i in range(1,len_x + 1):
		for j in range(1,len_y +1):
			label = board_matrix[i - 1][j] + board_matrix[i + 1][j] + board_matrix[i][j - 1] + board_matrix[i][j + 1] + board_matrix[i - 1][j - 1] + board_matrix[i - 1][j + 1] + board_matrix[i + 1][j - 1] + board_matrix[i + 1][j + 1]
			
			label_matrix[i-1][j-1] = label


	for i in range(len_x):
		for j in range(len_y):

			if board[i][j] == 1:
				if label_matrix[i][j] < 2 or label_matrix[i][j] > 3:
					board[i][j] = 0
			else:
				if label_matrix[i][j] == 3:
					board[i][j] = 1

	return board
# 

#Input: 
a = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]

print(next_state(a))

"""
#Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
"""