def next_state(board):
	len_x = len(board)
	len_y = len(board[0])

	# 0: state[0]->state[0]
	# 1: state[1]->state[0]
	# 2: state[0]->state[1]
	# 3: state[1]->state[1]

	for i in range(len_x):
		for j in range(len_y):
			# set boundary effect
			if i != 0 and j != 0 and i != len_x - 1 and j != len_y -1:
				label = board[i - 1][j]%2 + board[i + 1][j]%2 + board[i][j - 1]%2 + board[i][j + 1]%2 + board[i - 1][j - 1]%2 + board[i - 1][j + 1]%2 + board[i + 1][j - 1]%2 + board[i + 1][j + 1]%2
			# set 4 boundaries
			elif i == 0 and j != 0 and i != len_x - 1 and j != len_y -1:
				label = board[i + 1][j]%2 + board[i][j - 1]%2 + board[i][j + 1]%2 + board[i + 1][j - 1]%2 + board[i + 1][j + 1]%2
			elif i != 0 and j == 0 and i != len_x - 1 and j != len_y -1:
				label = board[i - 1][j]%2 + board[i + 1][j]%2 + board[i][j + 1]%2 + board[i - 1][j + 1]%2 + board[i + 1][j + 1]%2
			elif i != 0 and j != 0 and i == len_x - 1 and j != len_y -1:
				label = board[i - 1][j]%2 + board[i][j - 1]%2 + board[i][j + 1]%2 + board[i - 1][j - 1]%2 + board[i - 1][j + 1]%2
			elif i != 0 and j != 0 and i != len_x - 1 and j == len_y -1:
				label = board[i - 1][j]%2 + board[i + 1][j]%2 + board[i][j - 1]%2 + board[i - 1][j - 1]%2 + board[i + 1][j - 1]%2

			# set 4 corners
			elif i == 0 and j == 0 and i != len_x - 1 and j != len_y -1:
				label = board[i + 1][j]%2 + board[i][j + 1]%2 + board[i + 1][j + 1]%2
			elif i != 0 and j == 0 and i == len_x - 1 and j != len_y -1:
				label = board[i - 1][j]%2 + board[i][j + 1]%2 + board[i - 1][j + 1]%2
			elif i != 0 and j != 0 and i == len_x - 1 and j == len_y -1:
				label = board[i - 1][j]%2 + board[i][j - 1]%2 + board[i - 1][j - 1]%2
			elif i == 0 and j != 0 and i != len_x - 1 and j == len_y -1:
				label = board[i + 1][j]%2 + board[i][j - 1]%2 + board[i + 1][j - 1]%2

			print(label)

			if board[i][j] == 1:
				if label < 2 or label > 3:
					board[i][j] = 1	# 1: state[1]->state[0]
				else:
					board[i][j] = 3 # 3: state[1]->state[1]
			else:
				if label == 3:
					board[i][j] = 2	# 2: state[0]->state[1]
				else:
					board[i][j] = 0 # 0: state[0]->state[0]
	print(board) 
	for i in range(len_x):
		for j in range(len_y):
			board[i][j] = board[i][j]//2

	return board

"""
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